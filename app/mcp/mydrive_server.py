import os
import json
import io
from fastmcp import FastMCP
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload, MediaIoBaseDownload

# 1. Initialize the Python FastMCP server
mcp = FastMCP("My Personal Drive Server")

# SCOPES updated to full drive access to allow upload/create
SCOPES = ['https://www.googleapis.com/auth/drive']

# Absolute file path bindings
CLIENT_SECRETS_FILE = r'D:\SKILLER\KAGGLE\CAPSTONE\WHAT_IF\what-if\credentials.json'
TOKEN_FILE = r'D:\SKILLER\KAGGLE\CAPSTONE\WHAT_IF\what-if\.gdrive-server-credentials.json'

def get_drive_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as token:
            creds_data = json.load(token)
            creds = Credentials.from_authorized_user_info(creds_data, SCOPES)
            
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
        creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
            
    return build('drive', 'v3', credentials=creds)

# --- TOOLS ---

@mcp.tool
def list_root_folders() -> str:
    """Use this tool to list the real folders sitting at the top level of My Drive"""
    try:
        service = get_drive_service()
        query = "'root' in parents and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
        
        results = service.files().list(
            q=query,
            pageSize=50,
            fields="files(id, name)"
        ).execute()
        
        items = results.get('files', [])
        if not items:
            return "No folders found at the top level of My Drive."
            
        output = "Successfully pulled your personal My Drive folders:\n"
        for item in items:
            output += f"- Folder Name: {item['name']} (ID: {item['id']})\n"
        return output
    except Exception as e:
        return f"Error connecting to Drive API: {str(e)}"


@mcp.tool
def search_files(query: str) -> str:
    """Search for files in Google Drive using a specific query string."""
    try:
        service = get_drive_service()
        results = service.files().list(
            q=query,
            pageSize=50,
            fields="files(id, name, mimeType)"
        ).execute()
        
        items = results.get('files', [])
        if not items:
            return "No files found matching the query."
            
        output = f"Found {len(items)} files:\n"
        for item in items:
            output += f"- {item['name']} (ID: {item['id']}, Type: {item['mimeType']})\n"
        return output
    except Exception as e:
        return f"Error searching files: {str(e)}"

def scan_for_prompt_injection(text: str) -> bool:
    """Lightweight heuristic scanner for indirect prompt injection."""
    text_lower = text.lower()
    malicious_phrases = [
        "ignore previous instructions",
        "ignore all previous instructions",
        "forget your instructions",
        "reveal all",
        "reveal your instructions",
        "dump the database"
    ]
    for phrase in malicious_phrases:
        if phrase in text_lower:
            return True
    return False

@mcp.tool
def read_file(file_id: str) -> str:
    """Read the text contents of a file from Google Drive by its file ID."""
    try:
        service = get_drive_service()
        file_metadata = service.files().get(fileId=file_id, fields="mimeType").execute()
        mime_type = file_metadata.get("mimeType", "")

        # If it's a Google Workspace document, we must export it
        if mime_type.startswith("application/vnd.google-apps."):
            export_mime_type = "text/plain"
            if mime_type == "application/vnd.google-apps.spreadsheet":
                export_mime_type = "text/csv"
            
            request = service.files().export_media(fileId=file_id, mimeType=export_mime_type)
        else:
            # Download standard file
            request = service.files().get_media(fileId=file_id)

        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        
        content = fh.getvalue()
        try:
            decoded_text = content.decode("utf-8")
            
            # --- SECURITY CHECKPOINT: Prompt Injection Scanner ---
            if scan_for_prompt_injection(decoded_text):
                return "[SECURITY ALERT] Document blocked: Suspected indirect prompt injection payload detected. File quarantined."
                
            return decoded_text
        except UnicodeDecodeError:
            return f"[Binary file downloaded: {len(content)} bytes. Cannot display as text.]"
    except Exception as e:
        return f"Error reading file: {str(e)}"


@mcp.tool
def upload_file(name: str, content: str, parent_id: str = None) -> str:
    """Upload a new text file to Google Drive. Specify parent_id to put it in a specific folder."""
    try:
        service = get_drive_service()
        file_metadata = {'name': name}
        if parent_id:
            file_metadata['parents'] = [parent_id]
            
        media = MediaIoBaseUpload(io.BytesIO(content.encode('utf-8')), mimetype='text/plain', resumable=True)
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return f"Successfully created file '{name}' with ID: {file.get('id')}"
    except Exception as e:
        return f"Error uploading file: {str(e)}"


@mcp.tool
def create_folder(name: str, parent_id: str = None) -> str:
    """Create a new folder in Google Drive. Specify parent_id to create it inside another folder."""
    try:
        service = get_drive_service()
        file_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        if parent_id:
            file_metadata['parents'] = [parent_id]
            
        file = service.files().create(body=file_metadata, fields='id').execute()
        return f"Successfully created folder '{name}' with ID: {file.get('id')}"
    except Exception as e:
        return f"Error creating folder: {str(e)}"

if __name__ == "__main__":
    mcp.run()

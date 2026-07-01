---
name: gdrive_mcp
description: Reusable skill to connect to Google Drive via MCP to fetch, read, and upload files when requested by the user.
---

# Google Drive MCP Skill

This skill enables agents to interact with Google Drive using the custom Python FastMCP server provided in the codebase.

## Usage Instructions

When the user requests to fetch, read, or upload files to Google Drive, you can connect to the local Google Drive MCP server.

**Server Command:**
From the `what-if` project directory, run:
`uv run python app/mcp/mydrive_server.py`

**Available Tools:**
The custom Drive MCP server exposes the following tools:
- `list_root_folders`: Lists folders specifically sitting at the top level of My Drive. (No arguments)
- `search_files`: Search for files using a query.
- `read_file`: Read/download text content of a file (exports Docs/Sheets automatically).
- `upload_file`: Upload a text file to Drive.
- `create_folder`: Create a new folder in Drive.

**Authentication:**
Ensure that Google Cloud credentials are set up. The server typically looks for `.gdrive-server-credentials.json` or uses the `GDRIVE_CREDENTIALS_PATH` environment variable.

import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import os

async def test():
    project_root = os.path.abspath(".")
    oauth_path = os.path.join(project_root, "gcp-oauth.keys.json")
    credentials_path = os.path.join(project_root, ".gdrive-server-credentials.json")
    
    server_params = StdioServerParameters(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-gdrive"],
        env={
            **os.environ,
            "GDRIVE_OAUTH_PATH": oauth_path,
            "GDRIVE_CREDENTIALS_PATH": credentials_path,
        }
    )
    
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                print("Session initialized.")
                
                # List tools
                tools = await session.list_tools()
                print("Tools:", [t.name for t in tools.tools])
                
                # Call search tool
                print("Calling search tool with ''root' in parents'...")
                result = await session.call_tool("search", {"query": "'root' in parents"})
                print("Search result:", result.content)
    except Exception as e:
        import traceback
        traceback.print_exc()
        print("Error:", e)

asyncio.run(test())

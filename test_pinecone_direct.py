import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
from app.agent import pinecone_mcp

async def main():
    print("Initializing Pinecone MCP...")
    async with pinecone_mcp.session_params_context():
        # wait for session to start, maybe there's a list_tools
        tools = await pinecone_mcp._session.list_tools()
        print([t.name for t in tools.tools])

if __name__ == "__main__":
    asyncio.run(main())

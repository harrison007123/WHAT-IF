import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    server_params = StdioServerParameters(
        command="npx",
        args=["-y", "@pinecone-database/mcp"],
        env=dict(os.environ)
    )

    print("Connecting to Pinecone MCP...")
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            tools = await session.list_tools()
            print("Pinecone MCP Tools available:")
            for tool in tools.tools:
                print(f"- {tool.name}")

if __name__ == "__main__":
    asyncio.run(main())

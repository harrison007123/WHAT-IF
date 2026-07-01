import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

from app.agent import pinecone_test_agent

async def main():
    async for event in pinecone_test_agent.run(node_input="List the indexes in Pinecone."):
        print(event)

if __name__ == "__main__":
    asyncio.run(main())

---
name: pinecone_mcp
description: Reusable skill to connect to Pinecone via MCP to fetch, query, and upload vector data when requested by the user.
---

# Pinecone MCP Skill

This skill enables agents to interact with Pinecone vector databases using the Pinecone Model Context Protocol (MCP) server.

## Usage Instructions

When the user requests to fetch from or upload to Pinecone, you can run the Pinecone MCP server.

**Server Command:**
`npx -y @pinecone-database/mcp`

**Common Operations:**
Once connected to the MCP server (or if you are defining an ADK Agent that uses this MCP), the typical tools exposed are:
- `pinecone_query`: Fetch / search for similar vectors using a query.
- `pinecone_upsert`: Upload / insert vectors into the database.
- `pinecone_create_index`: Create a new vector index.

**Environment Variables:**
Ensure that `PINECONE_API_KEY` is set in the environment or `.env` file before launching the server.

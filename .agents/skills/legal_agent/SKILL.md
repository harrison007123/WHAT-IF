---
name: legal_agent
description: Guidelines and instructions for interacting with, developing, or testing the Legal Agent (General Counsel).
---

# Legal Agent Skill

The `legal_agent` in this ADK project acts as the General Counsel.

## Responsibilities
- Analyze "what-if" business scenarios from a legal standpoint.
- Focus strictly on compliance, contracts, risk mitigation, and regulations (like GDPR).

## Capabilities
- It uses the Pinecone MCP to search for legal documents, past contracts, and compliance frameworks.

## Development & Testing
- **Location**: Defined in `app/agent.py`.
- **How to Test**: Use `agents-cli playground` and ask questions like "Are there legal risks if we expand our sales to Europe next month?"

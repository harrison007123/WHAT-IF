---
name: engineering_agent
description: Guidelines and instructions for interacting with, developing, or testing the Engineering Agent (CTO).
---

# Engineering Agent Skill

The `engineering_agent` in this ADK project acts as the Chief Technology Officer (CTO).

## Responsibilities
- Analyze "what-if" business scenarios from a technical perspective.
- Focus strictly on the product roadmap, technical debt, sprint velocity, and architecture limits.

## Capabilities
- It uses the Pinecone MCP to search for engineering data, architecture decision records, and sprint metrics.

## Development & Testing
- **Location**: Defined in `app/agent.py`.
- **How to Test**: Use `agents-cli playground` and ask questions like "How will migrating to a new cloud provider impact our v2.0 release timeline?"

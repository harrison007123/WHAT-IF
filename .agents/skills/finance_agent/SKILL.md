---
name: finance_agent
description: Guidelines and instructions for interacting with, developing, or testing the Finance Agent (CFO).
---

# Finance Agent Skill

The `finance_agent` in this ADK project acts as the Chief Financial Officer (CFO).

## Responsibilities
- Analyze "what-if" business scenarios.
- Focus strictly on financial metrics: revenue, burn rate, MRR (Monthly Recurring Revenue), and profitability.

## Capabilities
- It uses the Pinecone MCP to search for historical or internal financial data to back up its analysis.

## Development & Testing
- **Location**: Defined in `app/agent.py`.
- **How to Test**: Use `agents-cli playground` and ask questions like "What happens to our MRR if we increase prices by 10%?"

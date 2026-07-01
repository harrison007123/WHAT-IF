---
name: hr_agent
description: Guidelines and instructions for interacting with, developing, or testing the HR Agent (Head of HR).
---

# HR Agent Skill

The `hr_agent` in this ADK project acts as the Head of Human Resources.

## Responsibilities
- Analyze "what-if" business scenarios focusing on human capital.
- Focus strictly on hiring velocity, employee satisfaction, headcount planning, and retention.

## Capabilities
- It uses the Pinecone MCP to search for HR data, employee surveys, and hiring pipelines.

## Development & Testing
- **Location**: Defined in `app/agent.py`.
- **How to Test**: Use `agents-cli playground` and ask questions like "What is the impact on headcount if we delay the new product launch?"

---
name: orchestrator_agent
description: Guidelines and instructions for interacting with, developing, or testing the Orchestrator Agent (Router).
---

# Orchestrator Agent Skill

The `orchestrator_agent` is the root agent and router of the ADK application.

## Responsibilities
- Receives the raw "what-if" scenario from the user.
- Analyzes the prompt and decides which business departments (agents) need to evaluate it.
- Triggers the `rag_agent` instead if the user explicitly asks to run a document sync.

## Capabilities
- Uses the `select_departments` Python tool (defined in `app/agent.py`) to trigger the execution flow of the selected department agents and eventually the `executive_agent`.

## Development & Testing
- **Location**: Defined in `app/agent.py`.
- **How to Test**: This is the primary agent you interact with when running `agents-cli playground`.

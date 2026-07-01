# What-If Simulator: Multi-Agent C-Suite

A highly capable, multi-agent AI system built on the [Google Agent Development Kit (ADK)](https://adk.dev/) designed to simulate a corporate C-Suite. Provide the system with complex "What-If" business scenarios, and watch as specialized department heads analyze the impact, retrieve corporate data using MCP, and synthesize a final executive recommendation for the board.

## 🧠 The Agent Architecture

This project utilizes native ADK 2.x sub-agent routing to orchestrate the following AI personas:

- **Orchestrator Agent**: The root router. Analyzes your scenario and dynamically transfers tasks to the relevant department agents.
- **Finance Agent (CFO)**: Analyzes the impact on revenue, burn rate, MRR, and profitability.
- **Engineering Agent (CTO)**: Analyzes the impact on technical debt, product roadmap, and sprint velocity.
- **HR Agent (Head of HR)**: Analyzes headcount constraints, employee morale, and hiring velocity.
- **Legal Agent (General Counsel)**: Analyzes compliance risks, contracts, and GDPR implications.
- **Executive Agent (CEO)**: Reads the gathered department reports and synthesizes them into a final board recommendation, complete with a list of contributing departments.
- **RAG Data Pipeline Agent**: A specialized utility agent that triggers an on-demand sync from Google Drive directly into our Pinecone vector database.

## 🔌 Integrations & MCP (Model Context Protocol)

This project heavily leverages MCP to give agents real-time access to corporate data:
- **Pinecone MCP**: Every agent has access to `pinecone_query` and `pinecone_upsert` to retrieve vectorized historical data during their analysis.
- **Google Drive FastMCP**: A custom Python server (`app/mcp/mydrive_server.py`) that allows the RAG agent to read Docs, Sheets, and files directly from Google Workspace.

## 🚀 Quick Start

Ensure you have **uv**, the Python package manager, installed.

1. **Install Dependencies:**
   ```bash
   agents-cli install
   ```

2. **Data Sync (Optional but Recommended):**
   Before running business scenarios, ensure your Pinecone DB has the latest data from Drive. Start the playground and run:
   > *"Sync our financial documents from Google Drive to Pinecone."*

3. **Run the Simulator:**
   Launch the local chat playground:
   ```bash
   agents-cli playground
   ```
   
   **Try asking a complex scenario:**
   > *"If we delay the launch of our v2.0 product by three months to rewrite the legacy backend, how will this impact our quarterly MRR projections, our sprint velocity, and the morale/retention of our development team?"*

## 🛠️ Commands & Project Management

| Command | Purpose |
|---------|---------|
| `agents-cli playground` | Launch the local chat interface |
| `agents-cli eval` | Evaluate agent behavior against datasets |
| `uv run pytest tests/unit` | Run unit and integration tests |
| `agents-cli deploy` | Deploy your agent to Google Cloud |
| `uv run python app/mcp/mydrive_server.py` | Manually start the custom Drive MCP server |

## 📁 Repository Structure

```
what-if/
├── .agents/                 # AI Assistant skills & guidelines (finance_agent, legal_agent, etc.)
├── app/                     # Core ADK application code
│   ├── agent.py             # Main multi-agent definitions and routing logic
│   └── mcp/                 # Custom FastMCP servers (e.g. Google Drive)
├── tests/                   # Pytest suites
└── pyproject.toml           # Project dependencies managed via uv
```

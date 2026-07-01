# The What-If Simulator: A Zero-Trust Virtual C-Suite
**Multi-Agent Business Strategy Orchestration using ADK & MCP**

**Agents Intensive - Capstone Project**  
**Hackathon Writeup**

---

### Project Overview
The **What-If Simulator** is a highly advanced, multi-agent AI system designed to act as a virtual corporate C-Suite. Built using the Google Agent Development Kit (ADK), this project allows executives and founders to input complex, hypothetical business scenarios (e.g., *"What is the impact of a 20% price increase?"* or *"What are the risks of acquiring a European competitor?"*). The system dynamically orchestrates specialized AI department heads to fetch real corporate data, analyze cross-functional impacts, and synthesize a comprehensive board-level recommendation in minutes.

A primary focus of this project is **Zero-Trust AI Security**, implementing rigorous safeguards at the input, data ingestion, and output layers to ensure sensitive corporate data remains sterile and secure.

---

### Problem Statement
In modern enterprises, executing a "What-If" analysis for a major strategic decision is a painfully slow, siloed process. If a CEO wants to understand the impact of delaying a product launch, they must manually coordinate with the CFO (for financial burn rate impact), the CTO (for engineering velocity), the CHRO (for employee retention), and the General Counsel (for contractual risks). 

This manual coordination takes weeks of meetings and email threads. Furthermore, providing AI assistants with access to raw corporate data (like Google Drive) introduces massive security vulnerabilities, including Data Leakage, Elevation of Privilege, and Indirect Prompt Injections (sleeper agent attacks hidden inside documents). 

### Solution Statement
The **What-If Simulator** solves the latency of executive decision-making by replacing manual coordination with a team of autonomous AI agents. These agents are equipped with the Model Context Protocol (MCP) to independently query a Pinecone vector database populated with the company's real financial, legal, and HR documents. 

To solve the security problem, the system implements a proprietary 3-Layer Zero-Trust architecture. It scans user inputs for jailbreaks, intercepts poisoned documents during data ingestion, and explicitly redacts Personally Identifiable Information (PII) before surfacing the final report to the user. The result is a system that delivers deep, data-backed strategic insights instantly, without compromising enterprise security.

---

### Architecture & Multi-Agent Coordination
Core to the What-If Simulator is an event-driven, multi-agent router built natively on the Google ADK 2.x architecture. Rather than relying on a monolithic prompt, the system delegates reasoning to specialized experts.

**The Perimeter Defense: `guardrail_agent`**
Serving as the `root_agent` of the application, this agent acts as an aggressive security bouncer. Its sole instruction is to evaluate the raw user prompt for malicious intent, jailbreaks, or dangerous system commands. If the prompt is deemed safe (including legitimate hypothetical business risks like "simulating a cyberattack"), it passes the payload to the Orchestrator. If malicious, it halts execution immediately.

**The Router: `orchestrator_agent`**
Once cleared by security, the Orchestrator evaluates the business scenario and determines which departments must be involved. It dynamically transfers the task to the relevant subset of department agents.

**The Department Heads**
Each department agent operates independently, armed with instructions specific to their domain and the ability to query the Pinecone MCP for historical context:
*   **`finance_agent`:** Analyzes MRR, burn rate, and profitability.
*   **`legal_agent`:** Scrutinizes contracts, compliance, and GDPR risks.
*   **`hr_agent`:** Evaluates headcount constraints and morale.
*   **`engineering_agent`:** Assesses technical debt and sprint velocity.

**The Synthesizer: `executive_agent`**
Acting as the CEO, this agent waits for the department heads to finish their independent analyses. It reads their reports, resolves conflicting data (e.g., Engineering pushing for a delay vs. Finance pushing for launch), and synthesizes a final, formatted Markdown recommendation highlighting risks, rewards, and a final verdict. It is strictly instructed to explicitly list the "Contributing Departments" to ensure auditability.

**The Output Filter: `dlp_agent`**
Before the CEO's report is shown to the user, it is routed through the Data Leakage Prevention (DLP) agent. This agent scrubs the final text, replacing exact salaries, Social Security Numbers, API keys, and sensitive PII with `[REDACTED]`, ensuring that internal agents can calculate using raw data, but the end-user only sees a sanitized report.

---

### Essential Tools & MCP Integrations

The true power of the Virtual C-Suite comes from its ability to read real corporate data using the Model Context Protocol (MCP).

**Pinecone Vector Database MCP**
All department agents are equipped with the `@pinecone-database/mcp` server. This allows them to execute semantic searches (`pinecone_query`) against the company's historical documents to ground their What-If analyses in factual data.

**Custom Google Drive FastMCP Server & The RAG Pipeline**
To keep Pinecone updated, the system features a dedicated `rag_agent` (Data Engineer). When a user requests a data sync, this agent utilizes a custom-built Python FastMCP server (`mydrive_server.py`) to read files directly from Google Workspace. 

**Zero-Trust Ingestion Scanner**
A standout feature of the Drive MCP server is its built-in defense against Indirect Prompt Injections. When the `read_file` tool downloads a document from Google Drive, the text is intercepted by a heuristic Python scanner *before* it is returned to the RAG Agent. If malicious payloads (e.g., "Ignore previous instructions") are detected hidden inside the document, the MCP server returns a `[SECURITY ALERT]` string instead of the file content. This completely shields the LLM from executing "sleeper agent" attacks hidden in corporate documents.

**Custom Markdown Skills (`.agents/skills`)**
To ensure the system remains highly extensible, the project leverages a custom `skills` architecture. Rather than hardcoding every possible sub-task into Python, specialized behaviors (like performing a `stride-threat-model` assessment) are written as declarative Markdown files in the `.agents/skills` directory. This allows the agents to dynamically read and execute complex, multi-step standard operating procedures on demand, making it easy to add new capabilities to the C-Suite without altering the core ADK logic.

---

### Zero-Trust Security Features Implemented

To protect the integrity of the Virtual C-Suite and prevent the leakage of confidential data, this project implements a rigorous 3-layer security model:

1. **Input Security (The Guardrail Agent):** We built a dedicated `guardrail_agent` that acts as the entry point for all user interactions. Before the Orchestrator evaluates a business scenario, the Guardrail Agent scans the prompt for jailbreaks, prompt injections, or malicious commands, dropping the request entirely if a threat is detected.
2. **Ingestion Security (Prompt Injection Scanner):** To prevent "sleeper agent" attacks where malicious instructions are hidden inside corporate documents, we built a heuristic Prompt Injection Scanner directly into the Google Drive FastMCP server. When a document is read, it is scanned *before* reaching the RAG Agent. If flagged, the MCP server returns a security alert, quarantining the file and preventing the vector database from being poisoned.
3. **Output Security (Data Leakage Prevention / DLP):** Internal department agents need to see raw financial data (e.g., exact salaries) to calculate accurate projections. However, to prevent this data from leaking to the end user, we implemented a `dlp_agent`. This agent intercepts the CEO's final report and scrubs it—replacing SSNs, exact salaries, API keys, and PII with `[REDACTED]` before the text is surfaced to the screen.

---

### Conclusion
The What-If Simulator demonstrates the profound potential of multi-agent systems when combined with strict enterprise security paradigms. By treating the AI ecosystem like a real corporate hierarchy—complete with security guards, domain experts, and executive synthesis—the ADK orchestrates a workflow that is highly analytical, fault-tolerant, and secure.

This project proves that LLMs no longer need to operate as simple chatbots; they can function as collaborative, tool-wielding teams that solve complex strategic problems while adhering to strict Data Leakage Prevention (DLP) and identity verification standards.

---

### Value Statement
The Virtual C-Suite drastically reduces strategic decision latency for executives. What previously took weeks of meetings and cross-departmental data gathering can now be simulated with high accuracy in minutes. This empowers founders to stress-test their roadmaps against legal, financial, and technical constraints instantly.

If granted more time for future development, I would focus on two key enhancements:
1.  **Expanding the C-Suite:** Adding a Marketing Agent and a Sales Agent equipped with MCP connections to Salesforce and Google Analytics to predict customer churn and campaign ROI.
2.  **Cloud Deployment Migration:** Migrating the local `stdio` MCP servers to cloud-hosted microservices running on Google Cloud Run via Server-Sent Events (SSE), and transitioning the Drive MCP from user OAuth to a Google Cloud Service Account for fully automated, headless background syncing.

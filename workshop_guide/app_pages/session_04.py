import streamlit as st
from components import render_session_header, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(4, "Cortex Agents", "30 min", "Cortex Agent created via UI with semantic view tool")

render_technologies_used([
    {"name": "Cortex Agent", "description": "An orchestrating AI that plans tasks, selects tools, executes them, reflects on results, and generates responses. Created as a first-class Snowflake object via the Snowsight UI.", "icon": "smart_toy"},
    {"name": "Tool Integration", "description": "The Agent uses tools like Cortex Analyst (semantic views) to answer questions. It automatically routes questions to the appropriate tool based on the query.", "icon": "route"},
    {"name": "Agent Instructions", "description": "Custom instructions that define the agent's role, behavior, domain expertise, and response style. Shapes how the agent interprets and answers questions.", "icon": "edit_note"},
])

st.markdown("---")

st.markdown("#### :material/smart_toy: Create a Cortex Agent")

st.markdown("""
In this session, you'll create a Cortex Agent using the Snowsight UI. The agent will use your semantic view from Session 3 as a tool, enabling conversational claims analytics.
""")

st.write("")

st.markdown("##### Step 1: Open the Agent Builder")
with st.container(border=True):
    st.markdown("""
1. In Snowsight, navigate to **AI & ML** in the left sidebar
2. Click **Cortex Agents**
3. Click **Create Agent** (or the **+** button)
""")

st.write("")

st.markdown("##### Step 2: Configure the agent")
with st.container(border=True):
    st.markdown("""
1. Set the database to **DENTAL_CLAIMS_AI** and schema to **CLAIMS_ANALYTICS**
2. Enter the object name: `CLAIMS_ANALYST_AGENT`
3. Enter the display name: `Claims Analyst Agent`
4. Click **Create agent**
""")

st.write("")

st.markdown("##### Step 3: Write agent instructions")
with st.container(border=True):
    st.markdown("""
1. Click the **Configuration** tab
2. Click the **Instructions** sub-tab

**Orchestration instructions** — paste the following into the orchestration instructions box:
""")
    st.code("""You are a dental claims analysis assistant for DentaQuest. Your role is to help claims analysts, managers, and executives understand claim patterns, provider performance, member utilization, and identify potential areas of concern.

When answering questions:
- Use the semantic view tool for all data queries about claims, members, providers, and procedures
- Provide specific numbers and percentages when available
- Highlight any unusual patterns or outliers
- When discussing financial data, format amounts as currency
- If asked about trends, compare across time periods when data allows
- Be concise but thorough — include context that helps with decision-making

Domain context:
- CDT codes (D0xxx-D9xxx) are the standard dental procedure coding system
- Plan types include PPO, HMO, DHMO, and Indemnity
- Network status affects reimbursement rates (In-Network vs Out-of-Network)
- Key metrics: approval rate, average days to adjudicate, denial rate by reason
- Common concerns: high-cost outlier providers, unusual procedure patterns, slow adjudication""", language="text", wrap_lines=True)
    st.markdown("""
**Response instructions** — paste the following into the response instructions box:
""")
    st.code("Always use charts and visualizations to show data whenever possible. Prefer bar charts for comparisons, line charts for trends over time, and tables for detailed breakdowns.", language="text", wrap_lines=True)

st.write("")

st.markdown("##### Step 4: Add the semantic view as a tool")
with st.container(border=True):
    st.markdown("""
1. Click the **Tools** sub-tab (still under Configuration)
2. Next to **Query structured data**, click the **+ Add semantic view** button
3. Select `CLAIMS_ANALYTICS_VIEW` (the semantic view created in Session 3)
4. Give the tool a name (e.g., `Claims Data`)
5. Click **Generate with Cortex** to create a detailed description for the tool — this helps the agent understand when to use it
6. Click **Add**
""")

st.markdown("""
**Other tools you can add to agents:**

| Tool type | Description |
|-----------|-------------|
| **Query structured data** | Semantic views — the agent generates SQL via Cortex Analyst to answer data questions |
| **Search documents** | Cortex Search services — the agent retrieves relevant passages from unstructured document collections |
| **Web search** | Enables the agent to search the internet for real-time information not in your Snowflake data |
| **Custom tools** | SQL UDFs or stored procedures — extend the agent with custom business logic, calculations, or external API calls |

For this workshop we'll use a single semantic view tool. In production, combining structured data + document search + custom tools creates powerful multi-capability agents.
""")

st.write("")

st.markdown("##### Step 5: Add sample questions")
with st.container(border=True):
    st.markdown("""
1. Click the **General** sub-tab (under Configuration)
2. Click **Add question** for each of the following sample questions:
""")
    st.code("What is our overall claim approval rate and how does it vary by plan type?", language="text", wrap_lines=True)
    st.code("Which providers have the highest average billed amount per claim?", language="text", wrap_lines=True)
    st.code("What are the most common denial reasons and their frequency?", language="text", wrap_lines=True)
    st.code("Show me the monthly trend in claim volume for 2025", language="text", wrap_lines=True)
    st.markdown("""
These sample questions appear in the agent's chat interface to help users get started.
""")

st.write("")

st.markdown("##### Step 6: Save the agent")
with st.container(border=True):
    st.markdown("""
Click the **Save** button to save all your configuration — instructions, tools, and sample questions. The agent must be saved before it can be tested.
""")

st.write("")

st.markdown("##### Step 7: Test the agent")
with st.container(border=True):
    st.markdown("""
1. Click the **Preview** tab to open the agent's chat interface
2. Test your agent by entering these queries one at a time:
""")
    st.code("What is our total claims volume and approval rate?", language="text", wrap_lines=True)
    st.code("Which providers are billing significantly above average for routine procedures?", language="text", wrap_lines=True)
    st.code("How has our denial rate changed month over month?", language="text", wrap_lines=True)
    st.code("Compare claim outcomes across plan types — which plans have the best approval rates?", language="text", wrap_lines=True)
    st.code("What are the top 3 areas where we could reduce claim denials?", language="text", wrap_lines=True)
    st.markdown("""
Observe how the agent routes each question to the semantic view, generates SQL, and synthesizes a conversational response with charts.
""")

st.write("")

st.markdown("---")

st.markdown("---")

render_explanation("How the agent works", """
**Cortex Agents** orchestrate multiple steps to answer questions:

1. **Understanding**: The agent reads the user's question and determines intent
2. **Planning**: It decides which tool(s) to use (in our case, the semantic view)
3. **Execution**: It calls Cortex Analyst to generate and run SQL against the semantic view
4. **Reflection**: It evaluates the results — are they sufficient? Need clarification?
5. **Response**: It synthesizes a natural language answer from the query results

**Agent vs. direct Cortex Analyst**:
- Cortex Analyst generates SQL and returns rows
- An Agent wraps Analyst with conversational context, instructions, and multi-turn memory

**Extending agents**: In production, you could add more tools:
- A **Cortex Search** service for searching unstructured documents
- **Custom UDFs** for business calculations (fraud scoring, risk assessment)
- **External APIs** via external access integrations
""")


render_key_concepts([
    {"term": "Cortex Agent", "definition": "A first-class Snowflake object that orchestrates LLMs and tools to answer complex questions. Supports planning, tool use, reflection, and multi-turn conversations. Created via UI or CREATE AGENT SQL."},
    {"term": "Agent Instructions", "definition": "A system prompt that defines the agent's role, behavior, domain expertise, and response style. Good instructions lead to more accurate, contextual responses."},
    {"term": "Tool Routing", "definition": "The agent's ability to select the appropriate tool for each question. With a semantic view tool, it routes data questions to Cortex Analyst for SQL generation."},
    {"term": "Sample Questions", "definition": "Seed questions displayed to users in the agent UI. Help users understand what the agent can do and provide starting points for exploration."},
])

render_what_you_built([
    "CLAIMS_ANALYST_AGENT — Cortex Agent with semantic view tool",
    "Custom instructions for dental claims analysis domain",
    "Tested analytics, trends, and cross-dimensional queries",
    "Agent ready for CoWork integration (Session 5)",
])

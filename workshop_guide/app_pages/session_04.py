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
1. **Name**: `CLAIMS_ANALYST_AGENT`
2. **Location**: `DENTAL_CLAIMS_AI.CLAIMS_ANALYTICS`
3. **Model**: Select `auto` (lets Snowflake choose the best available model)
""")

st.write("")

st.markdown("##### Step 3: Add the semantic view as a tool")
with st.container(border=True):
    st.markdown("""
1. In the **Tools** section, click **Add Tool**
2. Select **Semantic View** as the tool type
3. Choose `DENTAL_CLAIMS_AI.CLAIMS_ANALYTICS.CLAIMS_ANALYTICS_VIEW`
4. This gives the agent the ability to query your claims data via natural language
""")

st.write("")

st.markdown("##### Step 4: Write agent instructions")
with st.container(border=True):
    st.markdown("""
In the **Instructions** field, paste the following:

```text
You are a dental claims analysis assistant for DentaQuest. Your role is to help
claims analysts, managers, and executives understand claim patterns, provider
performance, member utilization, and identify potential areas of concern.

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
- Common concerns: high-cost outlier providers, unusual procedure patterns, slow adjudication
```
""")

st.write("")

st.markdown("##### Step 5: Add sample questions")
with st.container(border=True):
    st.markdown("""
Add these sample questions to help users understand what the agent can do:

1. "What is our overall claim approval rate and how does it vary by plan type?"
2. "Which providers have the highest average billed amount per claim?"
3. "What are the most common denial reasons and their frequency?"
4. "Show me the monthly trend in claim volume for 2025"
""")

st.write("")

st.markdown("##### Step 6: Test the agent")
with st.container(border=True):
    st.markdown("""
Use the built-in chat interface to test your agent with these queries:

1. **Basic analytics**: "What is our total claims volume and approval rate?"
2. **Provider analysis**: "Which providers are billing significantly above average for routine procedures?"
3. **Trend analysis**: "How has our denial rate changed month over month?"
4. **Cross-dimensional**: "Compare claim outcomes across plan types — which plans have the best approval rates?"
5. **Actionable insight**: "What are the top 3 areas where we could reduce claim denials?"

Observe how the agent routes each question to the semantic view, generates SQL, and synthesizes a conversational response.
""")

st.write("")

st.markdown("##### Step 7: Save and publish")
with st.container(border=True):
    st.markdown("""
1. Review your agent configuration
2. Click **Create** to save the agent
3. The agent is now available for use in CoWork (Session 5) and via the API
""")

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

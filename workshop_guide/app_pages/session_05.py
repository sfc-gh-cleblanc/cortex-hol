import streamlit as st
from components import render_session_header, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(5, "CoWork", "25 min", "Collaborative AI analysis with CoWork")

render_technologies_used([
    {"name": "Snowflake CoWork", "description": "An AI-powered collaborative workspace inside Snowsight where you can analyze data, generate insights, and share findings with your team — all through natural language conversation.", "icon": "group"},
    {"name": "Agent Integration", "description": "CoWork leverages your Cortex Agents to answer questions. The CLAIMS_ANALYST_AGENT from Session 4 powers the data analysis capabilities.", "icon": "smart_toy"},
    {"name": "Sharing & Collaboration", "description": "CoWork sessions can be shared with team members, creating a collaborative space for data exploration and decision-making.", "icon": "share"},
])

st.markdown("---")

st.markdown("#### :material/open_in_new: Open CoWork")
with st.container(border=True):
    st.markdown("""
In Snowsight, click **CoWork** in the left navigation panel. Start a new conversation.

CoWork provides a chat-based interface that leverages your Cortex Agent to query data, create visualizations, and generate insights. It uses the `CLAIMS_ANALYST_AGENT` you created in Session 4.

Paste each question below into CoWork one at a time and observe how it generates queries and visualizations.
""")

st.space("small")

st.markdown("#### :material/chat: Questions to ask CoWork")
st.caption("Copy and paste each question into CoWork individually. They build on each other in sequence.")

questions = [
    ("1. Portfolio Overview", "Show me an overview of our dental claims portfolio — total claims processed, approval rate, average payout amount, and total dollars paid."),
    ("2. Provider Outliers", "Which providers are billing significantly above average for common procedures like cleanings (D1110) and fillings (D2330, D2391)? Show me the outliers."),
    ("3. Denial Patterns", "What are the most common denial reasons and which procedure categories have the highest denial rates? Are there patterns we should investigate?"),
    ("4. Plan Comparison", "Compare claim outcomes across our plan types (PPO, HMO, DHMO, Indemnity). Which plans have the best approval rates and fastest adjudication?"),
    ("5. Geographic Analysis", "Break down our claims by member state. Which states have the highest average claim amounts and denial rates?"),
    ("6. Executive Summary", "Generate an executive summary of our dental claims operations that I could share with leadership. Include key metrics, trends, and the top 3 areas of concern."),
]

for title, question in questions:
    with st.container(border=True):
        st.markdown(f"**{title}**")
        st.code(question, language="text", wrap_lines=True)

st.space("small")

render_explanation("How CoWork works", """
**CoWork** is Snowflake's collaborative AI workspace. It uses your Cortex Agents to provide interactive data exploration.

**How CoWork differs from other tools**:
- **Cortex Code**: Developer tool — executes SQL, creates objects, builds infrastructure
- **CoWork**: Analyst tool — explores data, generates visualizations, shares insights
- **Cortex Agent (direct)**: API/programmatic access to the agent

**What CoWork does with these questions**:
1. Routes questions to your CLAIMS_ANALYST_AGENT
2. The agent generates SQL via the semantic view
3. Results are displayed with automatic visualizations
4. Supports follow-up questions in context

**Key capabilities**:
- Creates charts and visualizations automatically
- Maintains conversation context for follow-up questions
- Can be shared with team members for collaborative analysis
- Generates summaries and recommendations

**When to use CoWork vs. Cortex Code vs. Cortex Agent**:
| Tool | Best for |
|------|----------|
| Cortex Code | Building infrastructure, creating objects, writing SQL |
| CoWork | Exploring data, generating insights, team collaboration |
| Cortex Agent | End-user Q&A interface (deployed as a product) |
""")


render_key_concepts([
    {"term": "CoWork", "definition": "Snowflake's collaborative AI workspace for data exploration. Provides a conversational interface that queries data, creates visualizations, and generates insights. Designed for business analysts and team collaboration."},
    {"term": "Collaborative Intelligence", "definition": "The pattern where AI assists a team in making decisions together. CoWork sessions can be shared, allowing multiple people to ask questions, build on each other's analysis, and reach conclusions collectively."},
    {"term": "Context Maintenance", "definition": "CoWork maintains conversation history so follow-up questions build on previous analysis. Ask 'Show me claims by status' then 'Now filter to just denied' — it remembers the context."},
])

render_what_you_built([
    "Explored claims data through conversational AI in CoWork",
    "Generated visualizations and cross-table analysis",
    "Identified provider outliers and denial patterns",
    "Created an executive summary of claims operations health",
])

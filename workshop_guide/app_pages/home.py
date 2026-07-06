import streamlit as st

st.title("Port of Toronto AI Workshop")
st.markdown("Building Intelligence for Canada's Great Lakes Gateway with Snowflake Cortex")

st.space("small")

col1, col2, col3 = st.columns(3)
col1.metric("Sections", "6", help="Hands-on lab sections")
col2.metric("Prompts", "16", help="Total prompts across all tools")
col3.metric("Duration", "2.5 hrs", help="Total workshop time")

st.space("medium")

st.markdown("#### How this workshop works")

st.markdown("""
Each section has **numbered prompts** that you copy and paste into the appropriate tool:

- **Cortex Code** — for building infrastructure, creating objects, and writing SQL/Python
- **Cortex Analyst** — for testing natural language queries against your semantic view
- **Snowflake CoWork** — for collaborative data exploration and analysis

All prompts build on each other sequentially — run them in order throughout the morning.
""")

st.space("small")

st.markdown("#### The scenario")
with st.container(border=True):
    st.markdown("""
The **Port of Toronto** is a vital Great Lakes port operated by PortsToronto, handling bulk goods,
containers, and general cargo via the St. Lawrence Seaway system. Located on Toronto's waterfront
along Lake Ontario, it connects the Greater Toronto Area with Great Lakes and international shipping
routes, supporting the region's manufacturing, construction, and consumer supply chains.

We'll build a complete AI platform covering:

| Data type | Examples |
|-----------|---------|
| **Structured** | Container manifests, shipping schedules, CBSA declarations, cargo invoices, CN/CP Rail schedules |
| **Unstructured** | CBSA inspection reports, marine safety reports, incident logs |
| **Time series** | Crane utilization, truck queue times |
""")

st.space("small")

st.markdown("#### What we're building")

with st.container(border=True):
    st.markdown("""
In 2.5 hours, we build a complete AI-powered operations platform:

**1. Data Foundation** — Load structured and unstructured port operations data into Snowflake from pre-generated CSV files.

**2. Natural Language Analytics** — Create a Semantic View over operational tables and query them with plain English via Cortex Analyst.

**3. Intelligent Search** — Build a Cortex Search service over safety documents and inspection reports for hybrid semantic + keyword search.

**4. AI Agents** — Create a Cortex Agent that orchestrates structured data queries AND document search through a single conversational interface.

**5. Collaborative AI** — Use CoWork to collaboratively analyze port data with AI assistance.

**6. Operations Dashboard** — Deploy a Streamlit app with live KPIs, charts, and an AI chat interface.
""")

st.space("small")

st.markdown("#### Prerequisites")
with st.container(border=True):
    st.markdown("""
- Snowflake account with **ACCOUNTADMIN** role — see **Getting Started** in the sidebar to provision a free trial
- **Cortex Code** open in Snowsight and connected to your account
- Cross-region inference enabled (for Cortex LLM functions)
""")

st.space("medium")
st.caption("Built for the July 9, 2026 workshop  :material/location_on:  Snowflake Toronto Office — Lake of Bays boardroom")

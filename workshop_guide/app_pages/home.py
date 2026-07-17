import streamlit as st

st.title("Health Insurance Claims AI Workshop")
st.markdown("Building Intelligence for Claims Analysis with Snowflake Cortex")

st.write("")

col1, col2, col3 = st.columns(3)
col1.metric("Sections", "6", help="Hands-on lab sections")
col2.metric("Duration", "~4 hrs", help="Total workshop time including break")
col3.metric("Tools", "5", help="Cortex Code, Analyst, Agents, CoWork, Streamlit")

st.write(""); st.write("")

st.markdown("#### How this workshop works")

st.markdown("""
This guide provides **step-by-step instructions** for each session. You'll work through a mix of:

- **Cortex Code prompts** — copy into Cortex Code to build infrastructure and write SQL/Python
- **Snowsight UI walkthroughs** — follow guided steps to create semantic views and agents
- **Interactive exploration** — paste questions into CoWork for collaborative analysis

All sections build on each other sequentially — work through them in order.
""")

st.write("")

st.markdown("#### The scenario")
with st.container(border=True):
    st.markdown("""
A dental insurance company processes millions of claims annually. Claims analysts need to
extract insights from clinical notes, identify patterns in denials, monitor provider performance, and
detect potential fraud or waste — all while maintaining fast adjudication turnaround times.

We'll build a complete AI-powered claims intelligence platform covering:

| Data type | Examples |
|-----------|---------|
| **Structured** | Member enrollment, claims, providers, dental procedures, adjudication outcomes |
| **Unstructured** | Clinical narratives, adjuster notes, member appeals, EOB documents |
| **Reference** | CDT procedure codes, plan types, provider networks |
""")

st.write("")

st.markdown("#### What we're building")

with st.container(border=True):
    st.markdown("""
In this workshop, we build a complete AI-powered claims analytics platform:

**1. Data Foundation** — Load structured claims data and unstructured clinical documents into Snowflake.

**2. AI-Powered Extraction** — Use Cortex AI functions (AI_EXTRACT, AI_CLASSIFY, AI_COMPLETE) to transform unstructured claim notes and documents into queryable structured data at scale.

**3. Natural Language Analytics** — Create a Semantic View over claims tables using the Autopilot and query them with plain English via Cortex Analyst.

**4. AI Agents** — Create a Cortex Agent that provides self-service claims analytics through a conversational interface.

**5. Collaborative Analysis** — Use CoWork to explore claims data collaboratively with AI assistance.

**6. Operations Dashboard** — Deploy a Streamlit app with live KPIs, charts, and AI-powered insights.
""")

st.write("")

st.markdown("#### Prerequisites")
with st.container(border=True):
    st.markdown("""
- Snowflake account with **ACCOUNTADMIN** role — see **Getting Started** in the sidebar to provision a free trial
- **Cortex Code** open in Snowsight and connected to your account
- Cross-region inference enabled (for Cortex LLM functions)
""")

st.write(""); st.write("")
st.caption("Dental Claims AI Workshop — July 20, 2026")

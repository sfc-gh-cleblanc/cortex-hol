import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(3, "Cortex Analyst & Semantic Views", "35 min", "Semantic view created via Autopilot, tested with natural language queries")

render_technologies_used([
    {"name": "Semantic View Autopilot", "description": "A UI-guided tool in Snowsight that automatically generates a semantic view from your tables — detecting relationships, creating dimensions, facts, metrics, and synonyms.", "icon": "auto_awesome"},
    {"name": "Cortex Analyst", "description": "Snowflake's text-to-SQL engine that converts natural language questions into SQL queries. Uses a semantic view to understand your data's business meaning, relationships, and metrics.", "icon": "chat"},
    {"name": "Semantic View", "description": "A first-class Snowflake object that describes your data in business terms: tables, relationships, facts, dimensions, metrics, and synonyms. The bridge between natural language and SQL.", "icon": "description"},
])

st.markdown("---")

st.markdown("#### :material/auto_awesome: Create a Semantic View with Autopilot")

st.markdown("""
In this session, you'll use the **Semantic View Autopilot** to create a semantic view over your claims data — no SQL required. The Autopilot analyzes your tables and generates a complete semantic view with relationships, metrics, and dimensions.
""")

st.write("")

st.markdown("##### Step 1: Open the Semantic View Autopilot")
with st.container(border=True):
    st.markdown("""
1. In Snowsight, navigate to **AI & ML** in the left sidebar
2. Click **Cortex Analyst**
3. Click the **Create with Autopilot** button in the top right
""")

st.write("")

st.markdown("##### Step 2: Provide context")
with st.container(border=True):
    st.markdown("""
While providing context is optional, it's extremely useful in creating a high-quality semantic view. Without it, the model only uses the database schema information, which might lack business nuance. The Autopilot supports several options for providing context: Tableau workbooks, Power BI reports, existing SQL queries, and others.

For this workshop, we'll skip this step since our table and column names are descriptive enough for the Autopilot to work with.

1. Click **Skip** to proceed to the next step
""")

st.write("")

st.markdown("##### Step 3: Name your semantic view")
with st.container(border=True):
    st.markdown("""
1. Enter the name: `CLAIMS_ANALYTICS_VIEW`
2. Set the database to **DENTAL_CLAIMS_AI**
3. Set the schema to **CLAIMS_ANALYTICS**
4. Click **Next**
""")

st.write("")

st.markdown("##### Step 4: Select tables")
with st.container(border=True):
    st.markdown("""
1. Select these tables:
   - `MEMBERS`
   - `CLAIMS`
   - `PROVIDERS`
   - `DENTAL_PROCEDURES`
   - `EXTRACTED_CLAIM_INSIGHTS` (from Session 2)
2. Click **Next**
""")

st.write("")

st.markdown("##### Step 5: Select columns")
with st.container(border=True):
    st.markdown("""
1. Click **Select all** to include all columns from all selected tables
2. Click **Create** to complete the wizard

The Autopilot will analyze your tables and generate a semantic view with auto-detected relationships, dimensions, facts, metrics, and synonyms. This may take a moment.
""")

st.write("")

st.markdown("##### Step 6: Confirm relationships")
with st.container(border=True):
    st.markdown("""
When the Autopilot completes its analysis, it will make several suggestions. Scroll down to the **Relationships** section. There will be 4 relationships detected — these define the table joins that Cortex Analyst will use when generating SQL.

For each relationship:
1. Click the relationship
2. Click **Review**
3. Click **Add** to include it within the semantic view

Repeat for all 4 relationships to ensure Cortex Analyst can join across your tables correctly.
""")

st.markdown("---")

st.markdown("#### :material/chat: Test with Natural Language Queries")

PROMPT_3_1 = """Ask Cortex Analyst these questions using DENTAL_CLAIMS_AI.CLAIMS_ANALYTICS.CLAIMS_ANALYTICS_VIEW:

1. "What are the top 5 procedures by total billed amount?"
2. "Which providers have the highest claim denial rate?"
3. "Show me monthly claim volume trends by plan type for 2025"
4. "What is the average time from date of service to adjudication for approved vs denied claims?"
5. "What are the most common procedures for members in Massachusetts?"

Show the generated SQL and results for each."""

render_prompt("Prompt 3.1", "Test with Natural Language Queries", PROMPT_3_1)

st.info("""
:material/lightbulb: **You can also test these in the Cortex Analyst UI!**

In Snowsight, navigate to **AI & ML > Cortex Analyst** in the left sidebar. Select your `CLAIMS_ANALYTICS_VIEW` semantic view, and you'll see a playground where you can type natural language questions and see the generated SQL and results interactively.
""")

render_explanation("What these queries test", """
Each query exercises different capabilities of the semantic view:

1. **"Top 5 procedures by billed amount"** — Tests joining CLAIMS to DENTAL_PROCEDURES and aggregating billed_amount with a GROUP BY and ORDER BY.

2. **"Providers with highest denial rate"** — Tests a calculated metric (COUNT of denied / total COUNT) grouped by provider, requiring a JOIN to PROVIDERS.

3. **"Monthly claim volume by plan type"** — Tests time-series aggregation with DATE_TRUNC, GROUP BY on a dimension from MEMBERS (plan_type), and a JOIN between CLAIMS and MEMBERS.

4. **"Avg time to adjudication"** — Tests DATEDIFF between date_of_service and adjudication_date, grouped by status dimension.

5. **"Common procedures in Massachusetts"** — Tests filtering on a dimension (state) with a JOIN path through CLAIMS to MEMBERS.

**What to observe**: Look at the generated SQL — does it correctly identify which tables to join, which metrics to use, and how to filter? This demonstrates the power of the semantic layer.
""")


render_key_concepts([
    {"term": "Semantic View Autopilot", "definition": "A UI tool that automatically generates a semantic view by analyzing table structures, detecting foreign key relationships, inferring appropriate dimensions/facts/metrics, and adding synonyms. Significantly reduces the time to create a working semantic view."},
    {"term": "Cortex Analyst", "definition": "Snowflake's text-to-SQL engine. Takes natural language questions and generates SQL queries using a semantic view for context. Supports aggregations, joins, filtering, time-series analysis, and diverse query types."},
    {"term": "Fact vs Dimension vs Metric", "definition": "Facts are raw numeric columns (billed_amount). Dimensions are categorical/temporal columns for grouping and filtering (plan_type, state). Metrics are pre-defined aggregations over facts (SUM(billed_amount), AVG(paid_amount))."},
    {"term": "Synonyms", "definition": "Alternative names for dimensions and facts that help Cortex Analyst understand user intent. For example, 'dentist' as a synonym for provider_name, or 'payout' for paid_amount."},
])

render_what_you_built([
    "CLAIMS_ANALYTICS_VIEW semantic view (via Autopilot)",
    "Auto-detected relationships between 5 tables",
    "Natural language queries tested across multiple patterns",
    "Validated text-to-SQL accuracy for claims analytics",
])

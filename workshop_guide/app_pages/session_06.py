import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(6, "Streamlit", "30 min", "Claims dashboard with KPIs, charts, and AI-powered insights")

render_technologies_used([
    {"name": "Streamlit in Snowflake (SiS)", "description": "Deploy Python-based data apps directly within Snowflake. Apps run on container runtime with full Python package support, access data natively via Snowpark, and inherit Snowflake's security model.", "icon": "web"},
    {"name": "Compute Pool", "description": "A managed pool of container nodes that powers SiS apps. Provides CPU/GPU resources, auto-scales, and supports any Python package from pip.", "icon": "memory"},
    {"name": "AI SQL Functions in Apps", "description": "Use Cortex AI functions (AI_CLASSIFY, AI_EXTRACT) directly within Streamlit apps to provide real-time AI-powered insights alongside traditional KPIs and charts.", "icon": "auto_fix_high"},
])

st.markdown("---")

st.markdown("#### :material/open_in_new: Open Workspaces")
with st.container(border=True):
    st.markdown("""
For this section, open **Workspaces** in Snowsight (left navigation panel > Projects > Workspaces). Workspaces provides an IDE-like environment where Cortex Code can create and edit Streamlit app files directly.

Paste the prompts below into Cortex Code **within Workspaces** so the generated code is written directly into your app files.
""")


PROMPT_6_1 = """In DENTAL_CLAIMS_AI.CLAIMS_ANALYTICS, create a Streamlit app called CLAIMS_DASHBOARD. This Dashboard should display the following:

- KPI cards at the top showing: Total Claims (from CLAIMS), Approval Rate (% with status 'Approved'), Avg Days to Adjudicate (DATEDIFF between DATE_OF_SERVICE and ADJUDICATION_DATE for processed claims), Total Paid (SUM of PAID_AMOUNT)
- A pie chart showing claims by status (Approved, Denied, Pending, In Review)
- A bar chart of top 10 procedures by total billed amount (join CLAIMS to DENTAL_PROCEDURES for procedure descriptions)
- A line chart showing monthly claim volume over time
- An AI Insights section at the bottom that uses AI_CLASSIFY on 5 recent claim notes to show real-time claim categorization

Include a tab in the dashboard that gives descriptions of each of the metrics, where the data is coming from and how often it is updated.

Use st.connection("snowflake") for the Snowflake connection and make it visually clean with st.columns for layout."""

render_prompt("6.1", "Create the Streamlit App", PROMPT_6_1)

render_explanation("What this prompt does", """
Creates a full **Streamlit in Snowflake** application on the **container runtime**:

**Step 1 — Compute pool**:
```sql
CREATE COMPUTE POOL CLAIMS_COMPUTE_POOL
  MIN_NODES = 1 MAX_NODES = 1
  INSTANCE_FAMILY = CPU_X64_S;
```

**Step 2 — External Access Integration** (so container can install pip packages):
```sql
CREATE NETWORK RULE pypi_network_rule
  MODE = EGRESS TYPE = HOST_PORT
  VALUE_LIST = ('pypi.org', 'files.pythonhosted.org');

CREATE EXTERNAL ACCESS INTEGRATION pypi_access_integration
  ALLOWED_NETWORK_RULES = (pypi_network_rule) ENABLED = TRUE;
```

**Step 3 — Stage files and deploy**:
- Write streamlit_app.py and pyproject.toml to a stage
- Create the Streamlit object on the compute pool

**Dashboard pattern**:
```python
conn = st.connection("snowflake")
session = conn.session()
claims_df = session.sql("SELECT COUNT(*) as total FROM CLAIMS").collect()
st.metric("Total Claims", f"{claims_df[0]['TOTAL']:,}")
```

**AI Insights section** uses AI_CLASSIFY directly in the app:
```python
insights = session.sql(\"\"\"
    SELECT note_id, LEFT(note_text, 50) as preview,
           AI_CLASSIFY(note_text, ['Routine', 'Emergency', 'Surgical']) as category
    FROM CLAIM_NOTES ORDER BY CREATED_DATE DESC LIMIT 5
\"\"\").to_pandas()
st.dataframe(insights)
```

**Key advantages of SiS**:
- **No data movement**: App runs inside Snowflake
- **Security**: Inherits user's role and permissions
- **No infrastructure**: Compute pool auto-manages lifecycle
- **AI-native**: Call Cortex functions directly from app code
""")


PROMPT_6_2 = """Fix the errors shown on this dashboard"""

st.markdown("##### 6.2 — Test and Fix Errors")

with st.container(border=True):
    st.markdown("""
1. Open the `streamlit_app.py` file in the Workspaces editor
2. Click **Run** in the top-right to preview the dashboard

**Are there any errors?** It's common for the Streamlit skill to assume packages are available that aren't yet installed, or to reference columns slightly differently than expected. If you see errors on the dashboard:

3. Paste the following into Cortex Code:
""")
    st.code("Fix the errors shown on this dashboard", language="text", wrap_lines=True)
    st.markdown("""
4. Click **Keep All** to accept all of the code updates Cortex Code suggests
5. Click **Run** again in the code page to reload the dashboard
6. Repeat steps 3-5 if any errors remain — keep iterating until the dashboard loads cleanly
""")

st.write("")

st.markdown("##### 6.3 — Deploy Your App")

with st.container(border=True):
    st.markdown("""
Once the dashboard is running without errors, deploy it so others can discover and use it:

1. Click the **Deploy** button in the top-right of the Workspaces editor
2. Select the database: **DENTAL_CLAIMS_AI**
3. Select the schema: **CLAIMS_ANALYTICS**
4. Click **Deploy** to publish

Once deployed, the app becomes a first-class Snowflake object. Other users in your account can discover it from the **Projects > Streamlit** menu in Snowsight and access it based on their role permissions.
""")

st.info("""
:material/lightbulb: **Sharing your app:** After deployment, grant access to other roles:
```sql
GRANT USAGE ON STREAMLIT DENTAL_CLAIMS_AI.CLAIMS_ANALYTICS.CLAIMS_DASHBOARD TO ROLE <role_name>;
```
This is how teams publish internal data apps — analysts build in Workspaces, deploy to a shared schema, and stakeholders access via the Streamlit projects menu.
""")

render_explanation("Troubleshooting tips", """
**Common errors and fixes:**

- **ModuleNotFoundError** (e.g., `plotly`, `pandas`) — The app references a package not installed in Workspaces. Cortex Code will add the missing import or switch to a built-in Streamlit chart method.
- **Column not found** — The SQL references a column name with wrong casing or spelling. Cortex Code will query INFORMATION_SCHEMA to find the correct name.
- **Connection errors** — Ensure `st.connection("snowflake")` is used (not `snowflake.connector`).

**The iterative pattern:** In Workspaces, you can continuously prompt Cortex Code to fix issues, accept changes, and re-run — this rapid feedback loop is how production Streamlit apps are built and refined.

This completes the workshop — you've built a full AI-powered claims analytics platform from data loading through to a deployed application!
""")

st.write("")

st.markdown("---")

st.markdown("#### :material/star: Bonus: Add an AI Chat Interface")

with st.container(border=True):
    st.markdown("""
Want to take your dashboard further? Add a chat box that lets users ask natural language questions about the data, powered by `AI_COMPLETE`.

Using what you've learned, write a prompt for Cortex Code in Workspaces that adds an "Ask AI" tab with a conversational chat interface. Consider:
- Using `st.chat_input` and `st.chat_message` for the UI
- Calling `SNOWFLAKE.CORTEX.COMPLETE` with a model like `claude-sonnet-4-6`
- Passing current KPI values as context so the model can reference actual data
- Maintaining chat history in `st.session_state`

After adding, click **Keep All** and **Run** to test. This demonstrates how `AI_COMPLETE` can power conversational interfaces directly within Streamlit apps — giving users an AI assistant embedded alongside their operational dashboards.
""")

st.markdown("---")


render_key_concepts([
    {"term": "Container Runtime", "definition": "The current SiS execution environment. Apps run on a compute pool, support any Python package via pip, and use versioned stage syntax. Replaces the legacy warehouse runtime."},
    {"term": "Compute Pool", "definition": "A managed pool of container nodes. Choose an instance family (CPU_X64_S, GPU_NV_S, etc.), set min/max nodes, and Snowflake handles provisioning and scaling."},
    {"term": "External Access Integration", "definition": "Required for container runtime apps that install pip packages. Container nodes can't reach the internet by default — you must allow egress to pypi.org via network rules."},
    {"term": "AI Functions in Apps", "definition": "Cortex AI functions (AI_CLASSIFY, AI_EXTRACT, AI_COMPLETE) can be called directly from Streamlit app SQL queries, enabling real-time AI-powered features without external services."},
])

render_what_you_built([
    "CLAIMS_COMPUTE_POOL — compute pool for container runtime",
    "CLAIMS_DASHBOARD — Streamlit app with KPIs and charts",
    "Claims operations dashboard with approval rates, volume trends, and top procedures",
    "AI Insights section using AI_CLASSIFY for real-time claim categorization",
])

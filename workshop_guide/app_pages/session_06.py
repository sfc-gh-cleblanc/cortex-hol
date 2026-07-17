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

render_prompt("Prompt 6.1", "Create the Streamlit App", PROMPT_6_1)

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


PROMPT_6_2 = """Show me the SQL to verify the Streamlit app and compute pool:

1. SHOW COMPUTE POOLS;
2. SHOW STREAMLITS IN SCHEMA DENTAL_CLAIMS_AI.CLAIMS_ANALYTICS;
3. Describe the streamlit CLAIMS_DASHBOARD;

Also provide me with the direct URL to open the Streamlit app in Snowsight."""

render_prompt("Prompt 6.2", "Verify & Access the App", PROMPT_6_2)

st.success("""
:material/rocket_launch: **Preview and Deploy your app!**

Once Cortex Code has generated your app files in Workspaces:

1. **Run** — Click the **Run** button in the top-right of the Workspaces editor to preview your app. This launches a local preview so you can see the dashboard in action.

2. **Deploy** — When you're happy with the preview, click **Deploy** to publish the app to your Snowflake account. This makes it accessible to anyone with the appropriate role via Snowsight.

Try modifying the app (add a chart, change KPI labels) and re-run to see changes live!
""")

render_explanation("What this prompt does", """
Verification and access:

**SHOW COMPUTE POOLS** — confirms the pool is ACTIVE with correct instance family.

**SHOW STREAMLITS** — lists the app with its URL endpoint.

**DESCRIBE STREAMLIT** — shows main file, compute pool (confirms container runtime), and status.

**Accessing the app**: SiS apps are accessible via Snowsight at:
```
https://app.snowflake.com/<account>/#/streamlit-apps/DENTAL_CLAIMS_AI.CLAIMS_ANALYTICS.CLAIMS_DASHBOARD
```

**Sharing the app** with other roles:
```sql
GRANT USAGE ON STREAMLIT CLAIMS_DASHBOARD TO ROLE <role_name>;
```

This completes the workshop — you've built a full AI-powered claims analytics platform from data loading through to a deployed application!
""")


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

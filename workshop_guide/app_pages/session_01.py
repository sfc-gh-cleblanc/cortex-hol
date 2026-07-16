import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(1, "Data Prep", "30 min", "Database, schema, warehouse, and 6 tables loaded from CSV")

render_technologies_used([
    {"name": "Database & Schema", "description": "Snowflake's organizational hierarchy for objects. A database contains schemas, and schemas contain tables, views, and other objects.", "icon": "database"},
    {"name": "CSV File Format", "description": "Snowflake can infer schema and load data directly from CSV files using file formats and COPY INTO commands.", "icon": "table_chart"},
    {"name": "Virtual Warehouse", "description": "Snowflake's compute engine. A warehouse provides the CPU and memory to execute queries and load data. Scales independently of storage.", "icon": "memory"},
])


PROMPT_1_1 = """Create the following Snowflake objects for our Health Insurance Claims AI workshop:

1. A database called DENTAL_CLAIMS_AI
2. A schema called CLAIMS_ANALYTICS inside that database
3. A stage called DATA in the schema CLAIMS_ANALYTICS with a directory table and server side encryption
4. A stage called CLAIM_DOCS in the schema CLAIMS_ANALYTICS with a directory table and server side encryption
5. A warehouse called CLAIMS_WH (size MEDIUM, auto-suspend after 60 seconds, auto-resume enabled)
6. Set the session context to use these objects

Execute all SQL and confirm each object was created."""

render_prompt("Prompt 1.1", "Create Database, Schema, Stages & Warehouse", PROMPT_1_1)

render_explanation("What this prompt does", """
Creates the foundational Snowflake objects:

```sql
CREATE DATABASE DENTAL_CLAIMS_AI;
CREATE SCHEMA DENTAL_CLAIMS_AI.CLAIMS_ANALYTICS;
CREATE STAGE DENTAL_CLAIMS_AI.CLAIMS_ANALYTICS.DATA
  DIRECTORY = (ENABLE = TRUE)
  ENCRYPTION = (TYPE = 'SNOWFLAKE_SSE');
CREATE STAGE DENTAL_CLAIMS_AI.CLAIMS_ANALYTICS.CLAIM_DOCS
  DIRECTORY = (ENABLE = TRUE)
  ENCRYPTION = (TYPE = 'SNOWFLAKE_SSE');
CREATE WAREHOUSE CLAIMS_WH
  WAREHOUSE_SIZE = 'MEDIUM'
  AUTO_SUSPEND = 60
  AUTO_RESUME = TRUE;

USE DATABASE DENTAL_CLAIMS_AI;
USE SCHEMA CLAIMS_ANALYTICS;
USE WAREHOUSE CLAIMS_WH;
```

**Why MEDIUM?** We're loading ~1,100 rows total across structured tables — even X-SMALL would work. MEDIUM gives us comfortable headroom for the Cortex AI functions we'll use later. With AUTO_SUSPEND = 60 seconds, it pauses immediately after queries finish, minimizing credit usage.
""")


PROMPT_1_2 = """In DENTAL_CLAIMS_AI.CLAIMS_ANALYTICS, the 6 CSV files have been uploaded to an internal stage called DATA.

For all 6 tables (MEMBERS, CLAIMS, PROVIDERS, DENTAL_PROCEDURES, CLAIM_NOTES, MEMBER_COMMUNICATIONS):

1. Create a file format (CSV with PARSE_HEADER=TRUE, FIELD_OPTIONALLY_ENCLOSED_BY='"')
2. Create the tables with appropriate column types inferred from the data. Ensure to convert the column names to uppercase.
3. Load the data

Use CREATE TABLE with INFER_SCHEMA from a stage and then COPY INTO them. The key requirement is that all 6 tables are created and populated.

Execute all SQL."""

st.markdown("""
**Before running the prompt below, download the workshop data files and upload them to the `DATA` stage:**

1. **Download** the workshop repository as a ZIP file:
   **[Download ZIP](https://github.com/sfc-gh-cleblanc/cortex-hol/archive/refs/heads/main.zip)**
2. **Unzip** the downloaded file. The required CSV data files are located in the `workshop_guide/data/` folder:
   `members.csv`, `claims.csv`, `providers.csv`, `dental_procedures.csv`, `claim_notes.csv`, `member_communications.csv`
3. In Snowsight, navigate to **Data > Databases > DENTAL_CLAIMS_AI > CLAIMS_ANALYTICS > Stages > DATA** and upload all 6 CSV files from that folder.
4. Then copy the prompt below into Cortex Code and execute.
""")

render_prompt("Prompt 1.2", "Load and Create Tables from CSV", PROMPT_1_2)

render_explanation("What this prompt does", """
Loads all 6 data tables from CSV files uploaded to the internal stage `DATA`. Cortex Code will use INFER_SCHEMA to detect column types automatically:

```sql
CREATE OR REPLACE FILE FORMAT csv_format
  TYPE = CSV
  PARSE_HEADER = TRUE
  FIELD_OPTIONALLY_ENCLOSED_BY = '"';

CREATE OR REPLACE TABLE MEMBERS
  USING TEMPLATE (
    SELECT ARRAY_AGG(OBJECT_CONSTRUCT(*))
    FROM TABLE(INFER_SCHEMA(
      LOCATION => '@DENTAL_CLAIMS_AI.CLAIMS_ANALYTICS.DATA/members.csv',
      FILE_FORMAT => 'csv_format'
    ))
  );

COPY INTO MEMBERS
  FROM @DENTAL_CLAIMS_AI.CLAIMS_ANALYTICS.DATA/members.csv
  FILE_FORMAT = csv_format;
```

**The 6 tables**:
| Table | Rows | Description |
|-------|------|-------------|
| MEMBERS | 200 | Plan members with enrollment and demographics |
| CLAIMS | 500 | Dental claims with amounts and adjudication status |
| PROVIDERS | 50 | Dentists and practices with network status |
| DENTAL_PROCEDURES | 80 | CDT procedure code reference |
| CLAIM_NOTES | 200 | Free-text clinical narratives from adjusters |
| MEMBER_COMMUNICATIONS | 100 | Appeals, inquiries, and correspondence |
""")


PROMPT_1_3 = """Run a query in DENTAL_CLAIMS_AI.CLAIMS_ANALYTICS that shows every table name and its row count, ordered by row count descending. Format it nicely."""

render_prompt("Prompt 1.3", "Verify All Data Tables", PROMPT_1_3)

render_explanation("What this prompt does", """
A quick verification query:

```sql
SELECT table_name, row_count
FROM DENTAL_CLAIMS_AI.INFORMATION_SCHEMA.TABLES
WHERE table_schema = 'CLAIMS_ANALYTICS'
  AND table_type = 'BASE TABLE'
ORDER BY row_count DESC;
```

You should see approximately **1,130 total rows** across 6 tables.
""")


PROMPT_1_4 = """In DENTAL_CLAIMS_AI.CLAIMS_ANALYTICS, list the files in the CLAIM_DOCS stage to confirm the upload was successful. Show the file names and sizes."""

st.markdown("""
**Upload the claim documents to the `CLAIM_DOCS` stage:**

1. From the unzipped workshop repository, locate the `workshop_guide/data/claim_documents/` folder (contains 8 PDF files and 7 TXT files)
2. In Snowsight, navigate to **Data > Databases > DENTAL_CLAIMS_AI > CLAIMS_ANALYTICS > Stages > CLAIM_DOCS** and upload all 15 files
3. Then copy the prompt below into Cortex Code to verify the upload
""")

render_prompt("Prompt 1.4", "Upload & Verify Claim Documents", PROMPT_1_4)

render_explanation("What this prompt does", """
Verifies the claim document upload:

```sql
LIST @DENTAL_CLAIMS_AI.CLAIMS_ANALYTICS.CLAIM_DOCS;
```

You should see 15 files listed (8 PDFs and 7 TXTs). These contain sample EOBs, clinical narratives, and appeal letters that we'll process with AI_EXTRACT in Session 2.
""")


render_key_concepts([
    {"term": "Internal Stage", "definition": "A named Snowflake stage that stores files within Snowflake's managed storage. Files are uploaded via Snowsight UI or PUT command and can be used with COPY INTO and INFER_SCHEMA."},
    {"term": "INFER_SCHEMA", "definition": "A Snowflake table function that automatically detects column names and types from files in a stage. Eliminates manual CREATE TABLE DDL for well-structured CSV/Parquet files."},
    {"term": "File Format", "definition": "A named object specifying how to parse files (CSV delimiters, headers, quoting, compression). Created once and reused across multiple COPY INTO operations."},
])

render_what_you_built([
    "DENTAL_CLAIMS_AI database and CLAIMS_ANALYTICS schema",
    "CLAIMS_WH warehouse (Medium, auto-suspend 60s)",
    "6 data tables loaded from CSV (~1,130 total rows)",
    "CLAIM_DOCS stage with 15 uploaded claim documents",
])

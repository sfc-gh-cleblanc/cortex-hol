import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(2, "AI SQL", "40 min", "Structured data extraction from unstructured claims text using Cortex AI functions")

render_technologies_used([
    {"name": "AI_EXTRACT", "description": "Extracts structured fields from unstructured text or documents. Define a responseFormat schema and get clean JSON back. Works on text columns and staged files via TO_FILE().", "icon": "auto_fix_high"},
    {"name": "AI_CLASSIFY", "description": "Classifies text into predefined categories. Useful for triaging claims by type, urgency, or department without manual rules.", "icon": "category"},
    {"name": "AI_COMPLETE", "description": "The general-purpose LLM function. Pass a model and prompt to generate free-form text — summaries, recommendations, analysis. Supports structured JSON output and multiple models.", "icon": "view_timeline"},
])


PROMPT_2_1 = """In DENTAL_CLAIMS_AI.CLAIMS_ANALYTICS, use Cortex AI functions to extract structured data from the CLAIM_NOTES table.

The NOTE_TEXT column contains free-text clinical narratives written by dental adjusters. Use AI_EXTRACT to pull out structured fields from these notes.

1. First, show me 5 sample rows from CLAIM_NOTES so we can see the text format.

2. Then run AI_EXTRACT on 5 sample notes with this responseFormat:
   - tooth_number: "What tooth number is referenced (e.g., #14, #3)?"
   - procedure_type: "What dental procedure is being discussed or recommended?"
   - clinical_finding: "What is the primary clinical finding or diagnosis?"
   - pre_auth_required: "Is pre-authorization required? (yes/no/not mentioned)"
   - urgency: "How urgent is the treatment? (routine/urgent/emergency)"

3. Show the extracted JSON results alongside the original text so we can verify accuracy.

Execute all SQL and show the results."""

render_prompt("Prompt 2.1", "Extract Structured Data from Claim Notes", PROMPT_2_1)

render_explanation("What this prompt does", """
Uses **AI_EXTRACT** to transform unstructured clinical narratives into structured data:

```sql
SELECT
    note_id,
    LEFT(note_text, 80) AS note_preview,
    AI_EXTRACT(
        text => note_text,
        responseFormat => {
            'tooth_number': 'What tooth number is referenced?',
            'procedure_type': 'What dental procedure is discussed or recommended?',
            'clinical_finding': 'What is the primary clinical finding or diagnosis?',
            'pre_auth_required': 'Is pre-authorization required? (yes/no/not mentioned)',
            'urgency': 'How urgent is the treatment? (routine/urgent/emergency)'
        }
    ) AS extracted
FROM CLAIM_NOTES
LIMIT 5;
```

**How AI_EXTRACT works**:
- You define a `responseFormat` — a JSON object where keys are field names and values are natural language descriptions of what to extract
- The model reads the text and returns structured JSON matching your schema
- It uses the `arctic-extract` model automatically (no model selection needed)
- Works on any text: clinical notes, emails, reports, legal documents

**Key insight**: The quality of your responseFormat descriptions directly impacts extraction accuracy. Be specific about format expectations (e.g., "tooth number as #N" vs just "tooth").
""")


PROMPT_2_2 = """Now let's do two more AI operations in DENTAL_CLAIMS_AI.CLAIMS_ANALYTICS:

PART A - Classify claims by type:
Use AI_CLASSIFY on the NOTE_TEXT from CLAIM_NOTES to categorize each note into one of these categories: 'Routine Preventive', 'Restorative', 'Emergency', 'Surgical', 'Orthodontic', 'Periodontic'.
Show the top 10 results with the classification and confidence.

PART B - Extract from staged documents:
Review the claim_documents uploaded to the CLAIM_DOCS stage. Use AI_EXTRACT with TO_FILE() to extract:
- document_type: "What type of document is this? (EOB, clinical narrative, appeal letter)"
- member_name: "What is the patient/member name?"
- procedure_code: "What CDT procedure code is referenced?"
- claim_amount: "What is the billed or claimed dollar amount?"
- outcome: "What was the outcome or decision? (approved/denied/pending/not stated)"

Execute all SQL and show results."""

render_prompt("Prompt 2.2", "Classify Claims & Extract from Documents", PROMPT_2_2)

render_explanation("What this prompt does", """
Demonstrates two additional AI patterns:

**Part A — AI_CLASSIFY**:
```sql
SELECT
    note_id,
    LEFT(note_text, 60) AS preview,
    AI_CLASSIFY(
        text => note_text,
        categories => ['Routine Preventive', 'Restorative', 'Emergency',
                       'Surgical', 'Orthodontic', 'Periodontic']
    ) AS classification
FROM CLAIM_NOTES
LIMIT 10;
```

AI_CLASSIFY returns a JSON object with `label` (the chosen category) and `score` (confidence 0-1).

**Part B — Document extraction with TO_FILE()**:
```sql
SELECT
    RELATIVE_PATH,
    AI_EXTRACT(
        file => TO_FILE('@CLAIM_DOCS', RELATIVE_PATH),
        responseFormat => {
            'document_type': 'What type of document is this?',
            'member_name': 'What is the patient/member name?',
            'procedure_code': 'What CDT procedure code is referenced?',
            'claim_amount': 'What is the billed dollar amount?',
            'outcome': 'What was the outcome? (approved/denied/pending/not stated)'
        }
    ) AS extracted
FROM DIRECTORY('@CLAIM_DOCS')
LIMIT 3;
```

**When to use AI_EXTRACT vs AI_CLASSIFY**:
- **AI_EXTRACT**: Pull multiple structured fields from text (extraction)
- **AI_CLASSIFY**: Assign text to one of N predefined categories (classification)
""")


PROMPT_2_3 = """Now let's build a batch extraction pipeline in DENTAL_CLAIMS_AI.CLAIMS_ANALYTICS.

Create a materialized table called EXTRACTED_CLAIM_INSIGHTS that runs AI_EXTRACT across ALL rows in CLAIM_NOTES and flattens the results into proper columns:

1. Run AI_EXTRACT on the full CLAIM_NOTES table with the same responseFormat from Prompt 2.1 (tooth_number, procedure_type, clinical_finding, pre_auth_required, urgency)

2. Flatten the extracted JSON into individual columns using ::VARCHAR casting

3. Include the original note_id, claim_id, adjuster, and created_date alongside the extracted fields

4. Also use AI_COMPLETE to generate an actionable recommendation column. For each row, use AI_COMPLETE with model 'claude-sonnet-4-6' to produce a one-sentence recommendation based on the clinical_finding and urgency. For example: "Schedule follow-up within 2 weeks for root canal evaluation" or "Approve routine cleaning - no action needed". Include this as a RECOMMENDATION column in the table.

5. Create this as a table: CREATE TABLE EXTRACTED_CLAIM_INSIGHTS AS SELECT ...

6. After creation, show the row count and a sample of 10 rows from the new table.

Execute all SQL."""

render_prompt("Prompt 2.3", "Batch Extraction Pipeline", PROMPT_2_3)

render_explanation("What this prompt does", """
Creates a materialized extraction table — the core pattern for production AI pipelines:

```sql
CREATE OR REPLACE TABLE EXTRACTED_CLAIM_INSIGHTS AS
WITH extracted AS (
    SELECT
        NOTE_ID,
        CLAIM_ID,
        ADJUSTER,
        NOTE_TEXT,
        CREATED_DATE,
        AI_EXTRACT(
            NOTE_TEXT,
            {
                'tooth_number': 'What tooth number is referenced (e.g., #14, #3)?',
                'procedure_type': 'What dental procedure is being discussed or recommended?',
                'clinical_finding': 'What is the primary clinical finding or diagnosis?',
                'pre_auth_required': 'Is pre-authorization required? (yes/no/not mentioned)',
                'urgency': 'How urgent is the treatment? (routine/urgent/emergency)'
            }
        ) AS result
    FROM CLAIM_NOTES
)
SELECT
    NOTE_ID,
    CLAIM_ID,
    ADJUSTER,
    CREATED_DATE,
    result:response:tooth_number::VARCHAR AS TOOTH_NUMBER,
    result:response:procedure_type::VARCHAR AS PROCEDURE_TYPE,
    result:response:clinical_finding::VARCHAR AS CLINICAL_FINDING,
    result:response:pre_auth_required::VARCHAR AS PRE_AUTH_REQUIRED,
    result:response:urgency::VARCHAR AS URGENCY,
    AI_COMPLETE(
        'claude-sonnet-4-6',
        'You are a dental claims advisor. Based on the following clinical finding and urgency level, provide exactly one actionable recommendation sentence (no more than 20 words). Clinical finding: '
        || result:response:clinical_finding::VARCHAR || '. Urgency: ' || result:response:urgency::VARCHAR || '.'
    )::VARCHAR AS RECOMMENDATION
FROM extracted;
```

**AI_COMPLETE** is the general-purpose LLM function. Unlike AI_EXTRACT (structured extraction) and AI_CLASSIFY (categorization), AI_COMPLETE generates free-form text. Here it produces actionable next steps tailored to each claim's specific clinical context — all computed inline as part of the CTAS.

**Why materialize?** Running AI_EXTRACT and AI_COMPLETE on every query would be slow and expensive. By materializing once, you:
- Pay for extraction once, query the results for free
- Enable downstream joins and analytics on extracted fields
- Can refresh periodically as new notes arrive (or use Dynamic Tables for automation)

**Production pattern**: In production, you would use a **Dynamic Table** or **Stream + Task** to incrementally process new claim notes as they arrive, rather than reprocessing the full table.
""")


render_key_concepts([
    {"term": "AI_EXTRACT", "definition": "A Cortex AI function that extracts structured fields from unstructured text or files. You define a responseFormat schema (field names + descriptions) and it returns JSON. Uses the arctic-extract model automatically."},
    {"term": "AI_CLASSIFY", "definition": "A Cortex AI function that assigns text to one of N predefined categories. Returns the chosen label and a confidence score (0-1). No model selection needed."},
    {"term": "TO_FILE()", "definition": "A function that creates a file reference from a stage path. Used with AI_EXTRACT and AI_COMPLETE to process staged documents (PDFs, images, text files) rather than text columns."},
    {"term": "Batch Extraction", "definition": "The pattern of running AI functions across an entire table and materializing results into a new table. Converts unstructured data into queryable structured columns at scale."},
    {"term": "AI_COMPLETE", "definition": "The general-purpose Cortex AI function for text generation. Pass a model name and prompt to generate free-form text — recommendations, summaries, analysis. Supports structured JSON output via response schema."},
])

render_what_you_built([
    "AI_EXTRACT pipeline extracting 5 fields from clinical notes",
    "AI_CLASSIFY categorizing claims into 6 procedure types",
    "Document extraction from staged PDF/TXT files using TO_FILE()",
    "EXTRACTED_CLAIM_INSIGHTS materialized table (200 rows of structured extractions)",
    "AI_COMPLETE generating per-claim recommendations from clinical context",
])

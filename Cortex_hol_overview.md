# Health Insurance Claims AI Workshop — Overview

**Audience:** Sun Life DentaQuest  
**Date:** July 20, 2026  
**Total Duration:** ~4 hours (including break)  
**Platform:** Snowflake (Trial Account)  
**Trial Signup:** https://signup.snowflake.com/?t=0b12bc1bb793241db3f0dc38d8028580cb8f77a111f2359704a5e2707182aa1a

---

## Workshop Context

This hands-on workshop walks participants through building a complete AI-powered claims intelligence platform on Snowflake. The scenario centers on dental insurance claims analysis — participants load claims data, extract insights from unstructured clinical notes using Cortex AI functions, build a natural language analytics layer with Semantic Views, create an AI agent for self-service Q&A, and deploy a Streamlit dashboard.

The workshop is delivered as a multi-page Streamlit guide application. Each session contains numbered prompts that participants copy into Cortex Code (Snowflake's AI coding assistant) or follow as UI-guided steps within Snowsight.

---

## Time Estimates

| Session | Duration |
|---------|----------|
| Introductions & Overview | 15 min |
| 1. Data Prep | 30 min |
| 2. AI SQL | 40 min |
| 3. Cortex Analyst & Semantic Views | 35 min |
| **Break** | **15 min** |
| 4. Cortex Agents | 30 min |
| 5. CoWork | 25 min |
| 6. Streamlit | 30 min |
| Summary & Next Steps | 15 min |
| **Total** | **~4 hrs** |

---

## Block 1: Data & Intelligence

### Session 1 — Data Prep (30 min)

**Objective:** Establish the Snowflake environment and load all workshop data.

Participants create a database (`DENTAL_CLAIMS_AI`), schema (`CLAIMS_ANALYTICS`), warehouse, and internal stage. They upload synthetic CSV files covering members, claims, providers, dental procedures, claim notes (free-text), and member communications. Tables are created using `INFER_SCHEMA` and populated via `COPY INTO`. The session ends with a verification query confirming all tables and row counts.

**Key outcome:** A fully populated Snowflake environment with 6+ tables of structured and unstructured dental claims data ready for analysis.

---

### Session 2 — AI SQL (40 min)

**Objective:** Use Cortex AI functions to extract structured insights from unstructured claim documents and text at scale.

Following the pattern from Snowflake's "Batch Data Extraction at Scale with Cortex AI Functions" quickstart, participants:

1. Upload sample claim documents (EOBs, appeals, clinical narratives) to an internal stage
2. Use `AI_EXTRACT` with a `responseFormat` schema to pull structured fields from free-text claim notes (tooth number, procedure type, clinical finding, pre-authorization requirement, denial reason)
3. Use `AI_CLASSIFY` to categorize claims into types (routine, emergency, cosmetic, orthodontic)
4. Use `AI_EXTRACT` on staged documents (`.txt` files) via `TO_FILE()` to parse EOBs and appeals
5. Build a batch extraction pipeline that materializes all extracted fields into an `EXTRACTED_CLAIM_INSIGHTS` table

**Key outcome:** Unstructured clinical text transformed into queryable structured data using Cortex AI functions, demonstrating the AI_EXTRACT, AI_CLASSIFY, and batch processing patterns.

---

### Session 3 — Cortex Analyst & Semantic Views (35 min)

**Objective:** Create a semantic layer over claims data and query it with natural language.

This session is UI-guided. Participants use the **Semantic View Autopilot** in Snowsight to:

1. Navigate to the Autopilot and select tables from `DENTAL_CLAIMS_AI.CLAIMS_ANALYTICS`
2. Let the Autopilot generate a semantic view with auto-detected relationships, dimensions, facts, metrics, and synonyms
3. Review and accept the generated view
4. Test the semantic view with natural language questions in the Cortex Analyst playground:
   - "What are the top 5 procedures by total billed amount?"
   - "Which providers have the highest denial rate?"
   - "Show me monthly claim volume trends by plan type"
   - "What is the average time from service date to adjudication?"

**Key outcome:** A working semantic view that enables natural language queries over dental claims data, created entirely through the Autopilot UI without writing SQL.

---

## Break (15 min)

---

## Block 2: Agents & Apps

### Session 4 — Cortex Agents (30 min)

**Objective:** Create an AI agent that provides self-service claims analytics through a conversational interface.

Participants create a Cortex Agent using the Snowsight UI:

1. Navigate to AI & ML > Cortex Agents > Create Agent
2. Add the semantic view from Session 3 as a tool
3. Write agent instructions defining its role as a dental claims analysis assistant for DentaQuest — helping analysts understand claim patterns, provider performance, member utilization, and potential fraud/waste indicators
4. Add sample questions that demonstrate the agent's capabilities
5. Test the agent with various query types (aggregations, comparisons, trend analysis)

**Key outcome:** A deployed Cortex Agent that analysts can interact with conversationally to get claims insights, powered by the semantic view.

---

### Session 5 — CoWork (25 min)

**Objective:** Use the agent in CoWork for collaborative claims analysis and insight generation.

Participants open CoWork in Snowsight and interact with their agent for collaborative data exploration:
- "Show me an overview of our claims portfolio — total claims, approval rate, average payout"
- "Which providers are outliers in terms of billing amounts for common procedures?"
- "Are there patterns in denied claims by procedure type or provider?"
- "Compare approval rates across plan types — are some plans seeing more denials?"
- "Generate a summary of our dental claims operations health"

**Key outcome:** Hands-on experience with CoWork as a collaborative analysis tool, demonstrating how the Cortex Agent integrates into team workflows for self-service analytics.

---

### Session 6 — Streamlit (30 min)

**Objective:** Build and deploy a Streamlit dashboard with KPIs and AI-powered insights.

Participants use Cortex Code to create a Streamlit in Snowflake app (`CLAIMS_DASHBOARD`) with:
- KPI cards: Total Claims, Approval Rate, Avg Days to Adjudicate, Total Paid Amount
- Charts: Claims by status (pie), Monthly claim volume (line), Top procedures by cost (bar)
- An AI-powered insights section demonstrating AI_CLASSIFY or AI_EXTRACT inline
- Deploy on container runtime with a compute pool

**Key outcome:** A deployed Streamlit dashboard presenting key claims KPIs and charts, demonstrating Streamlit in Snowflake on container runtime.

---

## Summary of Snowflake Technologies Covered

| Technology | Session |
|-----------|---------|
| Database, Schema, Warehouse, Stage | 1 |
| INFER_SCHEMA, COPY INTO | 1 |
| AI_EXTRACT, AI_CLASSIFY | 2 |
| TO_FILE(), Batch Processing | 2 |
| Semantic View Autopilot | 3 |
| Cortex Analyst | 3 |
| Cortex Agents (UI) | 4 |
| CoWork | 5 |
| Streamlit in Snowflake (Container Runtime) | 6 |
| Compute Pools | 6 |

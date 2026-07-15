import streamlit as st

st.title("Workshop Agenda")

AGENDA = [
    ("Introductions & Overview", "15 min", None),
    ("Session 1: Data Prep", "30 min", "1"),
    ("Session 2: AI SQL", "40 min", "2"),
    ("Session 3: Cortex Analyst & Semantic Views", "35 min", "3"),
    (":orange-badge[BREAK]", "15 min", None),
    ("Session 4: Cortex Agents", "30 min", "4"),
    ("Session 5: CoWork", "25 min", "5"),
    ("Session 6: Streamlit", "30 min", "6"),
    ("Summary & Next Steps", "15 min", None),
]

for title, duration, session_num in AGENDA:
    if session_num:
        col1, col2 = st.columns([4, 1])
        col1.markdown(f":material/play_circle: **{title}**")
        col2.markdown(f":gray-badge[{duration}]")
    elif "BREAK" in title:
        col1, col2 = st.columns([4, 1])
        col1.markdown(f"{title}")
        col2.markdown(f":gray-badge[{duration}]")
    else:
        col1, col2 = st.columns([4, 1])
        col1.markdown(f":gray[{title}]")
        col2.markdown(f":gray-badge[{duration}]")

st.write(""); st.write("")

st.markdown("##### What you'll build")
st.markdown("""
| Object Type | Count | Examples |
|-------------|-------|---------|
| **Tables** | 6 | Members, claims, providers, procedures, claim notes, communications |
| **AI Extractions** | 1 | EXTRACTED_CLAIM_INSIGHTS materialized table |
| **Semantic Views** | 1 | Claims analytics semantic view (via Autopilot) |
| **Cortex Agents** | 1 | Claims analysis agent with semantic view tool |
| **Streamlit Apps** | 1 | Claims dashboard with KPIs and charts |
""")

st.write("")

st.markdown("##### Total duration")
with st.container(border=True):
    st.markdown("""
:material/schedule: **~4 hours** (including 15-minute break between Block 1 and Block 2)

Sun Life DentaQuest Workshop — July 20, 2026
""")

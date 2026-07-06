import streamlit as st

st.title("Workshop agenda")

AGENDA = [
    ("8:30 - 8:40 AM", "Arrival & Coffee", None, None),
    ("8:40 - 8:50 AM", "Welcome & Workshop Overview", None, None),
    ("8:50 - 9:10 AM", "Session 1: Data Prep", "20 min", "1"),
    ("9:10 - 9:35 AM", "Session 2: Cortex Analyst & Semantic Views", "25 min", "2"),
    ("9:35 - 9:55 AM", "Session 3: Cortex Search", "20 min", "3"),
    ("9:55 - 10:10 AM", ":orange-badge[BREAK]", None, None),
    ("10:10 - 10:30 AM", "Session 4: Cortex Agents", "20 min", "4"),
    ("10:30 - 10:45 AM", "Session 5: CoWork", "15 min", "5"),
    ("10:45 - 11:00 AM", "Session 6: Streamlit", "15 min", "6"),
]

for time, title, duration, session_num in AGENDA:
    if session_num:
        col1, col2 = st.columns([1, 4])
        col1.markdown(f"**{time}**")
        col2.markdown(f":material/play_circle: **{title}** :gray-badge[{duration}]")
    elif "BREAK" in title:
        col1, col2 = st.columns([1, 4])
        col1.markdown(f"**{time}**")
        col2.markdown(f"{title}")
    else:
        col1, col2 = st.columns([1, 4])
        col1.markdown(f"**{time}**")
        col2.markdown(f":gray[{title}]")

st.space("medium")

st.markdown("##### What you'll build by end of morning")
st.markdown("""
| Object Type | Count | Examples |
|-------------|-------|---------|
| **Tables** | 10 | Container manifests, invoices, rail schedules, incident logs |
| **Cortex Search Services** | 1 | Port knowledge base search |
| **Semantic Views** | 1 | PORT_OPERATIONS_VIEW with relationships, metrics, and AI instructions |
| **Cortex Agents** | 1 | Port operations agent with Analyst + Search + custom tools |
| **Streamlit Apps** | 1 | Operations dashboard with AI chat |
""")

st.space("small")

st.markdown("##### Location")
with st.container(border=True):
    st.markdown("""
:material/location_on: **Snowflake Toronto Office — Lake of Bays boardroom**

July 9, 2026 — 8:30 AM to 11:00 AM
""")

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import sys
from pathlib import Path

# Ensure project root is on sys.path so src can be imported from the dashboard folder
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from src.analytics import Analytics

analytics = Analytics()

st.set_page_config(
    page_title="FocusTrack AI",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 FocusTrack AI Dashboard")

st.markdown("---")

col1, col2, col3 = st.columns(3)

focus = st.session_state.get("focus", 100)
status = st.session_state.get("status", "Focused")
blinks = st.session_state.get("blinks", 0)

col1.metric(
    "Total Sessions",
    analytics.total_sessions()
)

col2.metric(
    "Average Focus",
    f"{analytics.average_focus()}%"
)

col3.metric(
    "Total Study Time",
    f"{analytics.total_duration()} min"
)

st.markdown("---")

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=focus,
    title={"text":"Focus Score"},
    gauge={
        "axis":{"range":[0,100]},
        "bar":{"color":"green"},
        "steps":[
            {"range":[0,50],"color":"red"},
            {"range":[50,75],"color":"yellow"},
            {"range":[75,100],"color":"green"}
        ]
    }
))

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

history = analytics.focus_history()

if history:

    import pandas as pd

    df = pd.DataFrame(
        history,
        columns=["Date","Focus"]
    )

    st.line_chart(
        df.set_index("Date")
    )

st.markdown("---")

st.write("Session Started")

st.write(datetime.now())
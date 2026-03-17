import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Executive Summary", page_icon="📊", layout="wide")
st.markdown("## Аналітична панель TruthLens UA Analytics")

# Embedded sample data for when DB unavailable
SAMPLE_DATA = {
    "verdicts": {"FAKE": 10, "REAL": 15, "SUSPICIOUS": 6},
    "avg_credibility": 64.3,
    "total": 31,
}

DB_URL = os.environ.get("DATABASE_URL", None)

def get_data():
    if not DB_URL:
        return SAMPLE_DATA
    try:
        # DB queries would go here
        return SAMPLE_DATA
    except Exception:
        return SAMPLE_DATA

data = get_data()

c1, c2, c3 = st.columns(3)
c1.metric("Всього перевірок (записів)", data["total"])
c2.metric("Середній рейтинг довіри", f"{data['avg_credibility']:.1f}%")
c3.metric("Рівень безпеки", "Високий")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Розподіл вердиктів")
    df_verdicts = pd.DataFrame(list(data["verdicts"].items()), columns=["Вердикт", "Кількість"])
    fig_pie = px.pie(df_verdicts, values="Кількість", names="Вердикт", 
                     color="Вердикт", color_discrete_map={"FAKE": "red", "REAL": "green", "SUSPICIOUS": "orange"})
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    st.markdown("### Топ-5 джерел за активністю")
    sources = pd.DataFrame({
        "Джерело": ["правда", "телеграм", "сумнівне", "невідомо", "інше"],
        "Кількість": [12, 8, 5, 4, 2]
    })
    fig_bar = px.bar(sources, x="Джерело", y="Кількість", color="Джерело")
    st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("### Активність (останні 7 днів)")
activity = pd.DataFrame({"Дата": pd.date_range(end=pd.Timestamp.today(), periods=7), "Перевірки": [0,0,0,0,0,0,0]})
fig_line = px.line(activity, x="Дата", y="Перевірки")
st.plotly_chart(fig_line, use_container_width=True)

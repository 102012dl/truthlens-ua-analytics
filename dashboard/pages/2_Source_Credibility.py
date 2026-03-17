import streamlit as st
import pandas as pd
import os
import plotly.express as px

st.set_page_config(page_title="Source Credibility", page_icon="📡", layout="wide")
st.markdown("## База надійності джерел (Source Credibility)")

def load_domains():
    try:
        df = pd.read_csv('data/processed/domain_trust_scores.csv')
        return df
    except Exception:
        return pd.DataFrame({
            "domain": ["pravda.com.ua", "ukrinform.ua", "hromadske.ua", "stopfake.org", "voxukraine.org", "suspilne.media"] + [f"regional-news-{i}.com.ua" for i in range(14)],
            "tier": ["TRUSTED", "TRUSTED", "TRUSTED", "FACT_CHECKER", "FACT_CHECKER", "TRUSTED"] + ["REGIONAL"] * 14,
            "credibility_score": [0.92, 0.91, 0.89, 0.92, 0.90, 0.91] + [0.70] * 14,
            "source_type": ["news"] * 3 + ["fact_checker"] * 2 + ["news"] * 15,
            "notes": ["Top tier", "State agency", "Independent", "Specialized", "Specialized", "Public broadcasting"] + ["Regional"] * 14
        })

df = load_domains()

min_cred = st.slider("Фільтр за мінімальним рейтингом довіри", 0.0, 1.0, 0.0, 0.05)
filtered_df = df[df["credibility_score"] >= min_cred].copy()

def color_score(val):
    if val > 0.75: color = 'lightgreen'
    elif val >= 0.45: color = 'lightyellow'
    else: color = 'lightcoral'
    return f'background-color: {color}'

st.markdown(f"**Знайдено джерел:** {len(filtered_df)}")
st.dataframe(filtered_df.style.map(color_score, subset=['credibility_score']), use_container_width=True)

st.markdown("### Розподіл рейтингу довіри")
fig = px.histogram(filtered_df, x="credibility_score", nbins=10, color_discrete_sequence=['#4C78A8'])
st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import pandas as pd
import os

st.title("🚀 H1B Processing Time Estimator")

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DATA_PATH = os.path.join(BASE_DIR, "DataSet", "h1b_data.csv")

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

# 🔄 Convert dates
df["case_submitted"] = pd.to_datetime(df["case_submitted"], errors='coerce')
df["decision_date"] = pd.to_datetime(df["decision_date"], errors='coerce')

# ⏳ Processing time
df["processing_days"] = (df["decision_date"] - df["case_submitted"]).dt.days

# 🎯 Inputs
status = st.selectbox("Case Status", df["case_status"].dropna().unique())
city = st.selectbox("Work City", df["work_city"].dropna().unique())

if st.button("Estimate Processing Time"):

    filtered = df[
        (df["case_status"] == status) &
        (df["work_city"] == city)
    ]

    if len(filtered) > 0:
        avg_days = int(filtered["processing_days"].mean())
        st.metric("Estimated Processing Days", avg_days)
        st.success("Estimate based on historical data ✅")
    else:
        st.error("No matching data found ❌")
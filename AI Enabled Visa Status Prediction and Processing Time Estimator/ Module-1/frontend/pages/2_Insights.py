import streamlit as st
import pandas as pd
import os

st.title("📊 H1B Visa Insights")

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DATA_PATH = os.path.join(BASE_DIR, "DataSet", "h1b_data.csv")

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

# Clean
df = df.dropna(subset=["case_status", "work_city", "job_title"])

# 📊 Case Status
st.subheader("Case Status Distribution")
st.bar_chart(df["case_status"].value_counts())

# 🌆 Cities
st.subheader("Top Work Cities")
st.bar_chart(df["work_city"].value_counts().head(10))

# 💼 Jobs
st.subheader("Top Job Titles")
st.bar_chart(df["job_title"].value_counts().head(10))

# 🏙️ States
st.subheader("Top States")
st.bar_chart(df["emp_state"].value_counts().head(10))
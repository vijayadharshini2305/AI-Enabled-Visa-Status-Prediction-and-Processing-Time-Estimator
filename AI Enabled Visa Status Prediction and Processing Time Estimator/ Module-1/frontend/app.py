import streamlit as st
import pandas as pd
import os

# 🔥 MUST be first Streamlit command
st.set_page_config(
    page_title="H1B Visa Analysis System",
    page_icon="🌍",
    layout="wide"
)

# 📁 Get base directory (Module-1)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# 📊 Dataset path
DATA_PATH = os.path.join(BASE_DIR, "DataSet", "h1b_data.csv")

# 📥 Load data safely
@st.cache_data
def load_data():
    if not os.path.exists(DATA_PATH):
        return None
    return pd.read_csv(DATA_PATH)

df = load_data()

# 🌍 Title
st.title("🌍 H1B Visa Data Analysis System")

# 🧠 Intro
st.markdown("""
Welcome to the **H1B Visa Data Analysis System** 👋  

This app helps you explore real-world H1B visa data.

👉 Use the sidebar to navigate:
- 📊 Insights  
- 📄 Report  
- 📌 About  
""")

st.divider()

# ⚠️ If dataset not found
if df is None:
    st.error("❌ Dataset not found! Please check path: DataSet/h1b_data.csv")

else:
    # 📊 Quick preview
    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    # 📈 Quick stats
    st.subheader("📊 Quick Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Records", len(df))

    with col2:
        st.metric("Unique Cities", df["work_city"].nunique())

    with col3:
        st.metric("Unique Job Roles", df["job_title"].nunique())

st.divider()

# ✨ Features section
st.subheader("✨ Features")

col1, col2 = st.columns(2)

with col1:
    st.success("📊 Analyze Case Status")
    st.success("🌆 Explore Work Cities")

with col2:
    st.success("💼 Job Trends")
    st.success("📄 Generate Reports")

# 📌 Footer
st.divider()
st.caption("Built using Streamlit • H1B Dataset • Data Analysis")
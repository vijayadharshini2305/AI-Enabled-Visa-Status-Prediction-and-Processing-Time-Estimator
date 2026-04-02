# 🇺🇸 AI-Enabled Visa Status Prediction & Processing Time Estimator

An end-to-end Machine Learning project that predicts visa approval status and estimates processing time using historical H-1B visa data.

---

## 📌 Project Overview

This project aims to:

* Predict whether a visa application will be **Approved or Denied**
* Estimate the **processing time (in days)**
* Demonstrate real-world application of Machine Learning

---

## 🌐 Live Demo

🚀 **Try the deployed app here:**
👉 https://vijayadharshini.streamlit.app/

---

## 🎯 Problem Statement

Visa processing is often uncertain and time-consuming. This project helps:

* Predict approval chances
* Estimate decision timelines

---

## 📊 Dataset Overview

* Dataset: H-1B Visa Applications (2011–2018)
* Size: ~3.3 Million Records

### Features:

* Case Status
* Application & Decision Dates
* Employer Details
* Job Title
* Wage Information
* Work Location

---

## 📥 Dataset Download

Dataset is hosted externally due to size limitations.

Download here:
https://drive.google.com/file/d/1U1mpPKvo7B731-3qr_p9wzB4ft3P4GTg/view?usp=sharing

After downloading:

* Place raw file in: `DataSet/h1b_data.csv`
* Or cleaned file in: `DataSet/preprocessed_data/cleaned_h1b_data.csv`

---

## 🔄 Module 1: Data Preprocessing

* Data cleaning
* Date conversion
* Feature creation (`processing_days`)
* Handling missing values
* Removing invalid records

---

## 🧠 Machine Learning Tasks

### Classification

* Target: `case_status`
* Output: Approved / Denied

### Regression

* Target: `processing_days`
* Output: Number of days

---

## 🛠️ Tech Stack

* Python
* pandas, numpy
* scikit-learn
* matplotlib, seaborn
* Streamlit
* Git & GitHub

---

## 📂 Project Structure

AI-Enabled-Visa-Status-Prediction/
│
├── DataSet/
│   ├── h1b_data.csv
│   └── preprocessed_data/
│       └── cleaned_h1b_data.csv
│
├── frontend/
│   └── app.py
│
├── models/
│
├── module1_preprocessing.py
├── module2_eda.py
├── module3_modeling.py
├── module4_predict.py
├── requirements.txt
├── .gitignore
├── .gitattributes
└── README.md

---

## ⚙️ Setup Instructions

### Clone repository

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

### Create virtual environment

python -m venv venv

Mac/Linux:
source venv/bin/activate

Windows:
venv\Scripts\activate

### Install dependencies

pip install -r requirements.txt

---

## ▶️ Run Project

Run preprocessing:

python module1_preprocessing.py

Run app:

streamlit run frontend/app.py

Open: http://localhost:8501

---

## 🚀 Future Work

* Add more ML models
* Improve accuracy
* Enhance UI/UX
* Add real-time data integration

---

## 👩‍💻 Author

**Vijayadharshini S**
B.E CSE | Data Science

---

## ⚠️ Disclaimer

For educational purposes only.

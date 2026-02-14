# AI Enabled Visa Status Prediction and Processing Time Estimator

## 📌 About This Project

This project focuses on building an AI-based system that can:

• Predict whether a visa application will be approved or denied  
• Estimate how many days the visa processing might take  

The system is developed using historical H-1B visa application data from 2011 to 2018.  
By analyzing past records, we aim to create intelligent models that can support decision-making in visa processing systems.

---

## 🎯 Why This Project?

Visa processing is often time-consuming and uncertain. Applicants often do not know:

- Whether their visa will be approved  
- How long the decision will take  

This project applies machine learning techniques to:

- Improve prediction accuracy  
- Provide estimated processing time  
- Demonstrate how AI can assist in real-world administrative systems  

---

## 📊 Dataset Overview

The dataset contains approximately **3.3 million visa application records**.

It includes:

- Application submission date  
- Decision date  
- Case status (Approved / Denied)  
- Employer details  
- Job title and classification  
- Wage information  
- Work location  
- Employer dependency information  

This dataset supports both classification and regression modeling.

---

## 📥 Dataset Download

Due to GitHub file size limitations, the full dataset is not uploaded to this repository.

You can download the full dataset and preprocessed dataset from Google Drive:

🔗 **Dataset Link:**  
https://drive.google.com/file/d/1U1mpPKvo7B731-3qr_p9wzB4ft3P4GTg/view?usp=sharing

After downloading:

1. Place the raw dataset (`h1b_data.csv`) inside the `DataSet/` folder.
2. Or place the cleaned dataset inside:
   `DataSet/preprocessed_data/`

---

## 🔄 Module 1: Data Collection & Preprocessing

In this module, the dataset was cleaned and prepared for model building.

### Steps Performed:

✔ Loaded the raw dataset  
✔ Removed unnecessary columns  
✔ Converted date columns into datetime format  
✔ Removed invalid or corrupted date records  
✔ Created a new feature: `processing_days`  
✔ Removed negative and unrealistic processing durations  
✔ Handled missing values  
✔ Optimized memory usage  
✔ Saved the cleaned dataset  

---

## 🧠 Target Variables

This project prepares data for two machine learning tasks:

### 1️⃣ Visa Status Prediction (Classification)

Target column: `case_status`  
Goal: Predict Approved or Denied  

### 2️⃣ Processing Time Estimation (Regression)

Target column: `processing_days`  
Goal: Predict number of days between submission and decision  

---

## 📂 Project Structure

AI Enabled Visa Status Prediction and Processing Time Estimator/
│
├── DataSet/
│   ├── h1b_data.csv  
│   └── preprocessed_data/
│        └── cleaned_h1b_data.csv  
│
├── module1_preprocessing.py  
├── README.md  

---

## ▶️ How to Run the Project (Module 1)

Step 1: Open Terminal and navigate to the project folder

```bash
cd "AI Enabled Visa Status Prediction and Processing Time Estimator"

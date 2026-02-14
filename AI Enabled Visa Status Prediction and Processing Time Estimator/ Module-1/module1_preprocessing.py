# ==========================================================
# Module 1: Data Collection & Preprocessing
# Project: AI Enabled Visa Status Prediction and
#          Processing Time Estimator
# ==========================================================

import pandas as pd
import numpy as np
import os


# ----------------------------------------------------------
# 1. Load Dataset
# ----------------------------------------------------------
def load_data(file_path):
    print("Loading dataset...")
    df = pd.read_csv(file_path, low_memory=False)
    print("Dataset loaded successfully!")
    print("Initial Shape:", df.shape)
    return df


# ----------------------------------------------------------
# 2. Drop Unnecessary Columns
# ----------------------------------------------------------
def drop_unnecessary_columns(df):

    columns_to_drop = [
        'emp_name',
        'emp_zip',
        'emp_country',
        'lng',
        'soc_name',
        'wage_unit',
        'pw_unit',
        'wage_to',
        'case_year'
    ]

    df = df.drop(columns=columns_to_drop, errors='ignore')
    print("Unnecessary columns removed.")
    return df


# ----------------------------------------------------------
# 3. Convert Date Columns Safely
# ----------------------------------------------------------
def convert_dates(df):

    df['case_submitted'] = pd.to_datetime(
        df['case_submitted'],
        errors='coerce'
    )

    df['decision_date'] = pd.to_datetime(
        df['decision_date'],
        errors='coerce'
    )

    # Remove rows where conversion failed
    df = df.dropna(subset=['case_submitted', 'decision_date']).copy()

    print("Date columns converted and invalid rows removed.")
    return df


# ----------------------------------------------------------
# 4. Create Processing Time Target Variable
# ----------------------------------------------------------
def create_processing_time(df):

    df = df.copy()

    df['processing_days'] = (
        df['decision_date'] - df['case_submitted']
    ).dt.days

    # Remove negative durations
    df = df[df['processing_days'] >= 0]

    # Remove extremely large unrealistic durations (more than 10 years)
    df = df[df['processing_days'] <= 3650]

    print("Processing time column created.")
    return df


# ----------------------------------------------------------
# 5. Handle Missing Values
# ----------------------------------------------------------
def handle_missing_values(df):

    df = df.copy()

    # Remove rows where target variable missing
    df = df.dropna(subset=['case_status'])

    # Fill numerical columns with median
    num_cols = df.select_dtypes(include=np.number).columns
    df.loc[:, num_cols] = df[num_cols].fillna(df[num_cols].median())

    # Fill categorical columns
    cat_cols = df.select_dtypes(include='object').columns
    df.loc[:, cat_cols] = df[cat_cols].fillna("Unknown")

    print("Missing values handled.")
    return df


# ----------------------------------------------------------
# 6. Optimize Memory Usage
# ----------------------------------------------------------
def optimize_memory(df):

    df = df.copy()

    for col in df.select_dtypes(include='object').columns:
        df.loc[:, col] = df[col].astype('category')

    print("Memory optimized.")
    return df


# ----------------------------------------------------------
# 7. Main Execution
# ----------------------------------------------------------
def main():

    base_dir = os.path.dirname(__file__)

    # Input dataset path
    input_path = os.path.join(
        base_dir,
        "DataSet",
        "h1b_data.csv"
    )

    # Run preprocessing pipeline
    df = load_data(input_path)
    df = drop_unnecessary_columns(df)
    df = convert_dates(df)
    df = create_processing_time(df)
    df = handle_missing_values(df)
    df = optimize_memory(df)

    print("\nFinal Shape:", df.shape)
    print("Final Memory Usage (MB):",
          round(df.memory_usage(deep=True).sum() / 1024**2, 2))

    # Create output directory
    output_folder = os.path.join(
        base_dir,
        "DataSet",
        "preprocessed_data"
    )

    os.makedirs(output_folder, exist_ok=True)

    # Output file path
    output_path = os.path.join(
        output_folder,
        "cleaned_h1b_data.csv"
    )

    # Save cleaned dataset
    df.to_csv(output_path, index=False)

    print("\n✅ Cleaned dataset saved at:")
    print(output_path)


# ----------------------------------------------------------
# Run Script
# ----------------------------------------------------------
if __name__ == "__main__":
    main()

# ==========================================================
# Module 2: Exploratory Data Analysis (EDA)
# Project: AI Enabled Visa Status Prediction and
#          Processing Time Estimator
# ==========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# ----------------------------------------------------------
# 1. Load Preprocessed Dataset
# ----------------------------------------------------------
def load_data(file_path):

    print("Loading cleaned dataset...")
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
    print("Dataset Shape:", df.shape)

    return df


# ----------------------------------------------------------
# 2. Display Basic Information
# ----------------------------------------------------------
def basic_information(df):

    print("\nDataset Information:")
    print(df.info())

    print("\nStatistical Summary:")
    print(df.describe())


# ----------------------------------------------------------
# 3. Visa Status Distribution
# ----------------------------------------------------------
def analyze_visa_status(df, output_folder):

    plt.figure()

    sns.countplot(x='case_status', data=df)

    plt.xticks(rotation=45)
    plt.title("Visa Status Distribution")
    plt.tight_layout()

    output_path = os.path.join(
        output_folder,
        "visa_status_distribution.png"
    )

    plt.savefig(output_path)
    plt.close()

    print("Visa status distribution plot saved.")


# ----------------------------------------------------------
# 4. Processing Time Distribution
# ----------------------------------------------------------
def analyze_processing_time(df, output_folder):

    plt.figure()

    sns.histplot(
        df['processing_days'],
        bins=50,
        kde=True
    )

    plt.title("Processing Time Distribution (Days)")
    plt.xlabel("Processing Days")
    plt.ylabel("Frequency")
    plt.tight_layout()

    output_path = os.path.join(
        output_folder,
        "processing_time_distribution.png"
    )

    plt.savefig(output_path)
    plt.close()

    print("Processing time distribution plot saved.")


# ----------------------------------------------------------
# 5. Correlation Heatmap
# ----------------------------------------------------------
def correlation_analysis(df, output_folder):

    numeric_df = df.select_dtypes(include=np.number)

    plt.figure(figsize=(10, 8))

    sns.heatmap(
        numeric_df.corr(),
        cmap="coolwarm"
    )

    plt.title("Correlation Heatmap")
    plt.tight_layout()

    output_path = os.path.join(
        output_folder,
        "correlation_heatmap.png"
    )

    plt.savefig(output_path)
    plt.close()

    print("Correlation heatmap saved.")


# ----------------------------------------------------------
# 6. Main Execution
# ----------------------------------------------------------
def main():

    base_dir = os.path.dirname(__file__)

    # Correct path based on your folder structure
    input_path = os.path.join(
        base_dir,
        "DataSet",
        "preprocessed_data",
        "cleaned_h1b_data.csv"
    )

    # Output folder for EDA results
    output_folder = os.path.join(
        base_dir,
        "eda_outputs"
    )

    os.makedirs(output_folder, exist_ok=True)

    # Run EDA pipeline
    df = load_data(input_path)
    basic_information(df)
    analyze_visa_status(df, output_folder)
    analyze_processing_time(df, output_folder)
    correlation_analysis(df, output_folder)

    print("\nFinal Shape:", df.shape)
    print("\nEDA Completed Successfully!")
    print("EDA outputs saved at:")
    print(output_folder)


# ----------------------------------------------------------
# Run Script
# ----------------------------------------------------------
if __name__ == "__main__":
    main()
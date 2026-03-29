# ==========================================================
# Module 3: Predictive Modeling
# Project: AI Enabled Visa Status Prediction and
#          Processing Time Estimator
# ==========================================================

import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor


# ----------------------------------------------------------
# 1. Load Dataset
# ----------------------------------------------------------
def load_data(file_path):

    print("Loading dataset for modeling...")
    df = pd.read_csv(file_path)

    print("Dataset loaded successfully!")
    print("Dataset Shape:", df.shape)

    return df


# ----------------------------------------------------------
# 2. Encode Categorical Variables
# ----------------------------------------------------------
def encode_categorical(df):

    df = df.copy()

    label_encoders = {}

    cat_cols = df.select_dtypes(include=['object', 'category']).columns

    for col in cat_cols:

        if col != "case_status":

            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))
            label_encoders[col] = le

    print("Categorical variables encoded.")

    return df, label_encoders


# ----------------------------------------------------------
# 3. Prepare Features and Target
# ----------------------------------------------------------
def prepare_features(df):

    df = df.copy()

    target = "processing_days"

    drop_cols = [
        "processing_days",
        "case_status",
        "case_submitted",
        "decision_date"
    ]

    X = df.drop(columns=drop_cols, errors='ignore')
    y = df[target]

    print("Features prepared.")
    print("Feature Shape:", X.shape)

    return X, y


# ----------------------------------------------------------
# 4. Train-Test Split
# ----------------------------------------------------------
def split_data(X, y):

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print("Train/Test split completed.")
    print("Train Shape:", X_train.shape)
    print("Test Shape:", X_test.shape)

    return X_train, X_test, y_train, y_test


# ----------------------------------------------------------
# 5. Train Models
# ----------------------------------------------------------
def train_models(X_train, y_train):

    models = {

        "Linear Regression": LinearRegression(),

        "Random Forest": RandomForestRegressor(
            n_estimators=100,
            random_state=42,
            n_jobs=-1
        ),

        "Gradient Boosting": GradientBoostingRegressor(
            n_estimators=100,
            learning_rate=0.1,
            random_state=42
        )
    }

    trained_models = {}

    for name, model in models.items():

        print("\nTraining", name, "...")
        model.fit(X_train, y_train)

        trained_models[name] = model

        print(name, "training completed.")

    return trained_models


# ----------------------------------------------------------
# 6. Evaluate Models
# ----------------------------------------------------------
def evaluate_models(models, X_test, y_test):

    results = {}

    for name, model in models.items():

        predictions = model.predict(X_test)

        mae = mean_absolute_error(y_test, predictions)
        rmse = np.sqrt(mean_squared_error(y_test, predictions))
        r2 = r2_score(y_test, predictions)

        results[name] = {
            "MAE": mae,
            "RMSE": rmse,
            "R2": r2
        }

        print("\n", name, "Performance")
        print("MAE:", round(mae, 2))
        print("RMSE:", round(rmse, 2))
        print("R2 Score:", round(r2, 3))

    return results


# ----------------------------------------------------------
# 7. Select Best Model
# ----------------------------------------------------------
def select_best_model(models, results):

    best_model_name = max(results, key=lambda x: results[x]["R2"])
    best_model = models[best_model_name]

    print("\nBest Model Selected:", best_model_name)

    return best_model_name, best_model


# ----------------------------------------------------------
# 8. Save Model + Metadata (IMPORTANT)
# ----------------------------------------------------------
def save_all(model, feature_columns, rmse, output_folder):

    os.makedirs(output_folder, exist_ok=True)

    # Save model
    model_path = os.path.join(output_folder, "visa_processing_time_model.pkl")
    joblib.dump(model, model_path)

    # Save features
    feature_path = os.path.join(output_folder, "model_features.pkl")
    joblib.dump(feature_columns, feature_path)

    # Save RMSE
    rmse_path = os.path.join(output_folder, "model_rmse.pkl")
    joblib.dump(rmse, rmse_path)

    print("\nModel and metadata saved successfully!")
    print("Model:", model_path)
    print("Features:", feature_path)
    print("RMSE:", rmse_path)


# ----------------------------------------------------------
# 9. Main Execution
# ----------------------------------------------------------
def main():

    base_dir = os.path.dirname(__file__)

    input_path = os.path.join(
        base_dir,
        "DataSet",
        "preprocessed_data",
        "cleaned_h1b_data.csv"
    )

    model_folder = os.path.join(base_dir, "models")

    # Load data
    df = load_data(input_path)

    # Encode
    df, encoders = encode_categorical(df)

    # Prepare features
    X, y = prepare_features(df)

    # Split
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Train
    models = train_models(X_train, y_train)

    # Evaluate
    results = evaluate_models(models, X_test, y_test)

    # Select best
    best_name, best_model = select_best_model(models, results)

    # Get RMSE of best model
    best_rmse = results[best_name]["RMSE"]

    # Save everything
    save_all(best_model, X.columns, best_rmse, model_folder)

    print("\nPredictive Modeling Completed Successfully!")


# ----------------------------------------------------------
# Run Script
# ----------------------------------------------------------
if __name__ == "__main__":
    main()
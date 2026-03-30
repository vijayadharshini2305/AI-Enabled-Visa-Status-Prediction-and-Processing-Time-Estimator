# ==========================================================
# Module 4: Processing Time Estimator Engine (FIXED)
# ==========================================================

import os
import joblib
import pandas as pd


# ----------------------------------------------------------
# 1. Define Paths
# ----------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")


# ----------------------------------------------------------
# 2. Load Saved Files
# ----------------------------------------------------------
def load_model():
    return joblib.load(os.path.join(MODEL_DIR, "visa_processing_time_model.pkl"))


def load_features():
    return joblib.load(os.path.join(MODEL_DIR, "model_features.pkl"))


def load_rmse():
    return joblib.load(os.path.join(MODEL_DIR, "model_rmse.pkl"))


def load_scaler():
    path = os.path.join(MODEL_DIR, "scaler.pkl")
    return joblib.load(path) if os.path.exists(path) else None


# ----------------------------------------------------------
# 3. Input Preprocessing (FIXED)
# ----------------------------------------------------------
def preprocess_input(user_input, feature_columns):

    # Create empty dataframe with correct columns
    df = pd.DataFrame(0, index=[0], columns=feature_columns)

    # ------------------------
    # Validate Date
    # ------------------------
    date_str = user_input.get("case_received_date")

    if not date_str:
        raise ValueError("case_received_date is required")

    date = pd.to_datetime(date_str, errors="coerce")

    if pd.isna(date):
        raise ValueError("Invalid date format. Use YYYY-MM-DD")

    # ------------------------
    # Date Features (ONLY if exist in model)
    # ------------------------
    date_features = {
        "year": date.year,
        "month": date.month,
        "quarter": (date.month - 1) // 3 + 1,
        "day": date.day,
        "weekday": date.weekday()
    }

    for col, value in date_features.items():
        if col in df.columns:
            df.loc[0, col] = value

    # ------------------------
    # Safe Text Formatting
    # ------------------------
    def format_text(value):
        return str(value).strip().lower().replace(" ", "_")

    # ------------------------
    # One-Hot Encoding (SAFE)
    # ------------------------
    mappings = [
        f"visa_class_{format_text(user_input.get('visa_type'))}",
        f"visa_status_{format_text(user_input.get('visa_status'))}",
        f"work_city_{format_text(user_input.get('city'))}"
    ]

    for col in mappings:
        if col in df.columns:
            df.loc[0, col] = 1

    # Ensure correct dtypes (fix warning)
    df = df.infer_objects(copy=False)

    return df


# ----------------------------------------------------------
# 4. Prediction Function
# ----------------------------------------------------------
def predict_processing_time(user_input):

    try:
        model = load_model()
        features = load_features()
        rmse = load_rmse()
        scaler = load_scaler()

        # Preprocess
        df = preprocess_input(user_input, features)

        # Apply scaler if exists
        if scaler is not None:
            df = scaler.transform(df)

        # Predict
        prediction = float(model.predict(df)[0])

        # Confidence Interval
        confidence = max(rmse * 0.25, prediction * 0.1)

        lower = max(0, prediction - confidence)
        upper = prediction + confidence

        return {
            "estimated_processing_days": round(prediction, 2),
            "confidence_range": f"{round(lower)} - {round(upper)} days"
        }

    except Exception as e:
        return {"error": str(e)}


# ----------------------------------------------------------
# 5. Testing
# ----------------------------------------------------------
if __name__ == "__main__":

    sample_input = {
        "case_received_date": "2023-07-15",
        "visa_type": "H1B",
        "visa_status": "Approved",
        "city": "New York"
    }

    result = predict_processing_time(sample_input)

    print("\n✅ Prediction Output:")
    print(result)
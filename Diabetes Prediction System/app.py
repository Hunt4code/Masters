from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

# Load trained model and scaler
model = joblib.load("random_forest_optimized.pkl")
scaler = joblib.load("scaler.pkl")

# Load original dataset to get feature names
df = pd.read_csv("diabetes_prediction_india.csv")
feature_columns = df.drop(columns=["Diabetes_Status"]).columns.tolist()

# Compute feature means (to fill missing values)
feature_means = df.drop(columns=["Diabetes_Status"]).mean().to_dict()

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        if "features" not in data:
            return jsonify({"error": "Missing 'features' key in request JSON"}), 400

        # Convert input list to dictionary
        input_data = dict(zip(feature_columns[:len(data["features"])], data["features"]))

        # Fill missing values with dataset mean
        for feature in feature_columns:
            if feature not in input_data:
                input_data[feature] = feature_means[feature]

        # Convert dictionary to numpy array
        input_array = np.array([list(input_data.values())])

        # Scale input data
        input_scaled = scaler.transform(input_array)

        # Predict using model
        prediction = model.predict(input_scaled)[0]

        return jsonify({"prediction": "Diabetic" if prediction == 1 else "Non-Diabetic"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

from soil_model_wrapper import SoilClassifierWithThreshold
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib
import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

# Load ML models
clf = joblib.load(os.path.join(BASE_DIR, "models", "soil_classifier_with_threshold.pkl"))
multi_rgr = joblib.load(os.path.join(BASE_DIR, "models", "soil_multi_regressor.pkl"))
ph_model = joblib.load(os.path.join(BASE_DIR, "models", "ph_regressor.pkl"))
moisture_model = joblib.load(os.path.join(BASE_DIR, "models", "moisture_regressor.pkl"))
temp_model = joblib.load(os.path.join(BASE_DIR, "models", "temperature_regressor.pkl"))
n_model = joblib.load(os.path.join(BASE_DIR, "models", "N_regressor.pkl"))
p_model = joblib.load(os.path.join(BASE_DIR, "models", "P_regressor.pkl"))
k_model = joblib.load(os.path.join(BASE_DIR, "models", "K_regressor.pkl"))
salinity_model=joblib.load(os.path.join(BASE_DIR, "models", "salinity.pkl"))
@app.route("/analyze", methods=["POST"])
def analyze():
    # File upload
    if "file" in request.files and request.files["file"].filename != "":
        file = request.files["file"]
        if file.filename.endswith('.csv'):
            data = pd.read_csv(file)
        else:
            return jsonify({"error": "Only CSV supported"}), 400
    else:
        # Manual entry
        try:
            pH = float(request.form.get("pH"))
            temperature = float(request.form.get("temperature"))
            moisture = float(request.form.get("moisture"))
            salinity = float(request.form.get("salinity", 0))
            N = float(request.form.get("N"))
            P = float(request.form.get("P"))
            K = float(request.form.get("K"))

            data = pd.DataFrame([{
                "moisture": moisture,
                "temperature": temperature,
                "pH": pH,
                "salinity": salinity,
                "N": N,
                "P": P,
                "K": K
            }])
        except Exception as e:
            return jsonify({"error": f"Invalid input: {str(e)}"}), 400

    # Features for prediction
    features = ["moisture", "temperature", "pH", "salinity", "N", "P", "K"]
    latest = data[features].iloc[-1]
    input_df = latest.to_frame().T  # Convert Series to 1-row DataFrame

    try:
        # Predict soil class
        pred_class = clf.predict(input_df)[0]

        # Predict each parameter separately
        pred_dict = {
            "pH": float(ph_model.predict(input_df)[0]),
            "moisture": float(moisture_model.predict(input_df)[0]),
            "temperature": float(temp_model.predict(input_df)[0]),
            "N": float(n_model.predict(input_df)[0]),
            "P": float(p_model.predict(input_df)[0]),
            "K": float(k_model.predict(input_df)[0]),
            "salinity":float(salinity_model.predict(input_df)[0])
        }

        # Generate remedies
        remedies = []
       # Remedies Suggestions
        if pred_dict["pH"] < 6.0:
            remedies.append("pH too low (acidic): Apply lime, wood ash, or compost to raise pH")
        elif pred_dict["pH"] > 7.5:
            remedies.append("pH too high (alkaline): Add sulfur, peat moss, or organic matter to lower pH")
        if pred_dict["moisture"] < 20:
            remedies.append("Moisture too low: Irrigate with drip/sprinkler system, apply mulching")
        elif pred_dict["moisture"] > 80:
            remedies.append("Moisture too high: Improve soil drainage, reduce irrigation, use raised beds")

        if pred_dict["N"] < 50:
            remedies.append("Nitrogen too low: Apply urea, manure, or nitrogen-rich compost") 
        elif pred_dict["N"] > 200:
            remedies.append("Nitrogen too high: Reduce fertilizer use, grow legumes to balance soil")

        if pred_dict["P"] < 30:
           remedies.append("Phosphorus too low: Apply bone meal, rock phosphate, or compost")
        elif pred_dict["P"] > 80:
           remedies.append("Phosphorus too high: Avoid P-fertilizers, use cover crops to absorb excess")

        if pred_dict["K"] < 100:
           remedies.append("Potassium too low: Add wood ash, potassium sulfate, or compost")
        elif pred_dict["K"] > 300:
            remedies.append("Potassium too high: Avoid K-fertilizers, add gypsum or organic matter")

# Salinity (EC)
        if pred_dict["salinity"] < 0.5:
           remedies.append("Salinity too low: Add balanced fertilizers or organic compost to increase nutrient ions")
        elif pred_dict["salinity"] > 4.0:
           remedies.append("Salinity too high: Leach soil with good-quality water, improve drainage, use salt-tolerant crops")

# Temperature
        if pred_dict["temperature"] < 15:
           remedies.append("Temperature too low: Use mulching, greenhouses, or crop covers")
        elif pred_dict["temperature"] > 35:
           remedies.append("Temperature too high: Irrigate frequently, provide shading, use heat-tolerant crop varieties")


        return jsonify({
            "prediction": str(pred_class),
            "parameters": pred_dict,
            "remedies": remedies,
            "latest": latest.to_dict()
            })
    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500


@app.route("/")
def home():
    return "Flask backend is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

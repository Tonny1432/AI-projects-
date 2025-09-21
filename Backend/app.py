from flask import Flask, request, render_template, jsonify
import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Backend/
PARENT_DIR = os.path.dirname(BASE_DIR)                 # SOIL_APP/
FRONTEND_DIR = os.path.join(PARENT_DIR, "Frontend")    # SOIL_APP/Frontend

app = Flask(__name__,
            template_folder=FRONTEND_DIR,
            static_folder=FRONTEND_DIR)

# Load models
clf = joblib.load(os.path.join(BASE_DIR, "models", "soil_classifier.pkl"))
rgr = joblib.load(os.path.join(BASE_DIR, "models", "soil_regressor.pkl"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    # Case 1: CSV file uploaded
    if "file" in request.files and request.files["file"].filename != "":
        file = request.files["file"]
        data = pd.read_csv(file)

    # Case 2: Manual entry
    else:
        try:
            pH = float(request.form.get("pH"))
            temperature = float(request.form.get("temperature"))
            moisture = float(request.form.get("moisture"))
            salinity = float(request.form.get("salinity"))
            N = float(request.form.get("N"))
            P = float(request.form.get("P"))
            K = float(request.form.get("K"))
            
            data = pd.DataFrame([{
                "pH": pH,
                "temperature": temperature,
                "moisture": moisture,
                "salinity": salinity,
                "N": N,
                "P": P,
                "K": K
            }])
        except:
            return jsonify({"error": "Invalid input values"}), 400

    # Keep only numeric columns
    numeric_cols = data.select_dtypes(include=["number"]).columns
    features = data[numeric_cols]
    latest = features.iloc[-1]

    # AI predictions
    pred_class = clf.predict([latest])[0]
    pred_moist = rgr.predict([latest])[0]
    

    # Remedies
    remedies = []
    if latest["pH"] < 6.0:
        remedies.append("pH is low (acidic): Add lime, wood ash, or compost.")
    elif latest["pH"] > 7.5:
        remedies.append("pH is high (alkaline): Add organic matter like compost.")

    if latest["temperature"] < 15:
        remedies.append("Temperature is low: Use mulch or cover soil.")
    elif latest["temperature"] > 35:
        remedies.append("Temperature is high: Provide shade or water.")

    if latest["moisture"] < 20:
        remedies.append("Moisture is low: Irrigate and mulch.")
    elif latest["moisture"] > 80:
        remedies.append("Moisture is high: Improve drainage.")

    if latest["salinity"] > 4:
        remedies.append("Salinity is high: Leach soil with water and add organic matter.")

    if latest["N"] < 50:
        remedies.append("Nitrogen is low: Add compost or organic manure.")
    if latest["P"] < 30:
        remedies.append("Phosphorus is low: Add compost or organic manure.")
    if latest["K"] < 100:
        remedies.append("Potassium is low: Add compost or organic manure.")

    return jsonify({
    "prediction": str(pred_class),
    "moisture": float(pred_moist),
    "remedies": remedies,
    "latest": latest.to_dict()
})


if __name__ == "__main__":
    app.run(debug=True)

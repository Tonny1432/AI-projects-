import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(MODEL_DIR, exist_ok=True)

# Load your dataset (make sure you have dataset.csv in Backend/)
data = pd.read_csv(os.path.join(BASE_DIR, "soil_data.csv"))

# Features
X = data[["moisture", "temperature", "pH", "salinity", "N", "P", "K"]]

# Define target variables (each one gets its own model)
targets = {
    "ph_regressor.pkl": "pH",
    "moisture_regressor.pkl": "moisture",
    "temperature_regressor.pkl": "temperature",
    "N_regressor.pkl": "N",
    "P_regressor.pkl": "P",
    "K_regressor.pkl": "K",
    "salinity.pkl":"salinity"
}

# Train and save each model
for filename, target in targets.items():
    y = data[target]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Save trained model
    joblib.dump(model, os.path.join(MODEL_DIR, filename))
    print(f"✅ Saved {filename}")

print("🎉 All models trained and saved successfully!")

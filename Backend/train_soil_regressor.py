import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib
import os

# Load dataset
df = pd.read_csv("soil_data.csv")  # dataset is in the same folder

# Features & target
feature_cols = ["moisture", "temperature", "pH", "salinity", "N", "P", "K"]
X = df[feature_cols]
y_reg = df["moisture"]  # replace with your actual regressor column

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y_reg, test_size=0.2, random_state=42)

# Build pipeline
rgr_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("rgr", RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train
rgr_pipeline.fit(X_train, y_train)

# Optional evaluation
print("Regressor R^2 score:", rgr_pipeline.score(X_test, y_test))

# Save the trained model
os.makedirs("models", exist_ok=True)
joblib.dump(rgr_pipeline, "models/soil_regressor.pkl")
print("Regressor saved to models/soil_regressor.pkl")

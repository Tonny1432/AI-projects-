import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# 1. Load Data
data = pd.read_csv("soil_data.csv")

# 2. Features and Labels
X = data[["pH", "moisture", "nitrogen", "phosphorus", "potassium"]]
y = data["soil_health"]

# 3. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Test Model
y_pred = model.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))

# 6. Save Model
joblib.dump(model, "soil_model.pkl")

# 7. Take User Input
print("\n🌱 Enter your soil test values:")
pH = float(input("Enter pH value: "))
moisture = float(input("Enter moisture (%): "))
nitrogen = float(input("Enter nitrogen level: "))
phosphorus = float(input("Enter phosphorus level: "))
potassium = float(input("Enter potassium level: "))

# 8. Predict Soil Health
user_sample = [[pH, moisture, nitrogen, phosphorus, potassium]]
prediction = model.predict(user_sample)

print("\n🔎 Prediction for your soil sample:", prediction[0])

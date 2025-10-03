import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib
import os

# Load dataset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # folder of this script
csv_path = os.path.join(BASE_DIR, "soil_data.csv")
df = pd.read_csv(csv_path)# dataset is in the same folder

# Features & target
feature_cols = ["moisture", "temperature", "pH", "salinity", "N", "P", "K"]
X = df[feature_cols]
y_class = df["label"]  # replace with your actual classifier column

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y_class, test_size=0.2, random_state=42)

# Build pipeline
clf_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train
clf_pipeline.fit(X_train, y_train)

# Optional evaluation
print("Classifier accuracy (ML only):", clf_pipeline.score(X_test, y_test))

# -------------------------
# 5️⃣ Threshold-based function
# -------------------------
def classify_soil_threshold(params):
    thresholds_dict = {
        'pH': {'optimal':(6,7.5), 'stable':(5.5,8), 'alert':(5,8.5), 'warning':(4.5,9)},
        'moisture': {'optimal':(30,50), 'stable':(20,60), 'alert':(10,70), 'warning':(5,80)},
        'salinity': {'optimal':(0,1), 'stable':(1,1.5), 'alert':(1.5,2), 'warning':(2,3)},
        'temperature': {'optimal':(20,30), 'stable':(15,35), 'alert':(10,40), 'warning':(5,45)},
        'N': {'optimal':(20,40), 'stable':(15,50), 'alert':(10,60), 'warning':(5,70)},
        'P': {'optimal':(15,30), 'stable':(10,35), 'alert':(5,40), 'warning':(2,45)},
        'K': {'optimal':(100,200), 'stable':(80,220), 'alert':(60,240), 'warning':(40,260)}
    }

    total_score = 0
    for key in params:
        value = params[key]
        t = thresholds_dict[key]
        if t['optimal'][0] <= value <= t['optimal'][1]:
            score = 0
        elif t['stable'][0] <= value <= t['stable'][1]:
            score = 1
        elif t['alert'][0] <= value <= t['alert'][1]:
            score = 2
        elif t['warning'][0] <= value <= t['warning'][1]:
            score = 3
        else:
            score = 4
        total_score += score

    if total_score <= 3:
        return "Optimal"
    elif total_score <= 7:
        return "Stable"
    elif total_score <= 12:
        return "Alert"
    elif total_score <= 17:
        return "Warning"
    else:
        return "Critical"

# -------------------------
# 6️⃣ Wrapper class to integrate thresholds
# -------------------------
class SoilClassifierWithThreshold:
    def __init__(self, pipeline):
        self.pipeline = pipeline

    def predict(self, X):
        # ML prediction (optional)
        ml_preds = self.pipeline.predict(X)

        # Apply threshold per sample
        final_preds = []
        for i, row in X.iterrows():
            params = row.to_dict()
            threshold_pred = classify_soil_threshold(params)
            final_preds.append(threshold_pred)  # threshold overrides ML
        return final_preds

# -------------------------
# 7️⃣ Wrap the trained pipeline
# -------------------------
soil_clf = SoilClassifierWithThreshold(clf_pipeline)

# -------------------------
# 8️⃣ Save wrapped classifier
# -------------------------
os.makedirs("models", exist_ok=True)
joblib.dump(soil_clf, "models/soil_classifier_with_threshold.pkl")
print("Wrapped classifier saved as soil_classifier_with_threshold.pkl")

# -------------------------
# 9️⃣ Example usage
# -------------------------
sample = pd.DataFrame([{
    'moisture': 55, 'temperature': 28, 'pH': 7.8,
    'salinity': 1.6, 'N': 45, 'P': 12, 'K': 180
}])

predicted_class = soil_clf.predict(sample)[0]
print("Predicted soil class for sample:", predicted_class)

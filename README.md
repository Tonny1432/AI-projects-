# 🧠 Bank Marketing Classification: Deep Learning vs Random Forest

This project compares the performance of a Deep Learning model and a Random Forest classifier on a real-world bank marketing dataset.

---

## 📌 Objective
To classify whether a customer will subscribe to a term deposit (yes/no) and compare model performance using different approaches.

---

## ⚙️ Technologies Used
- Python  
- PyTorch (Deep Learning)  
- Scikit-learn (Machine Learning)  
- Pandas (Data Processing)  
- Matplotlib (Visualization)  

---

## 📊 Dataset
- Bank Marketing Dataset  
- Preprocessed to handle:
  - Missing values  
  - Duplicate records  
  - Outliers (IQR method)  
  - Categorical encoding  

---

## 🔧 Data Preprocessing
- Removed duplicates and null values  
- Applied IQR method for outlier removal  
- Encoded categorical features using LabelEncoder  
- Converted target variable (`y`) into binary (0/1)

---

## 🤖 Models Used

### 1️⃣ Deep Learning Model (PyTorch)
- Multi-layer neural network:
  - Input → 32 → 16 → 8 → Output  
- Activation: ReLU  
- Loss Function: CrossEntropyLoss (with class weights)  
- Optimizer: Adam  

### 2️⃣ Machine Learning Model
- Random Forest Classifier  

---

## 📈 Evaluation Metrics
- Accuracy  
- Confusion Matrix  
- Classification Report  

---

## 📊 Results
- Compared performance of both models  
- Visualized accuracy using bar chart  

---

## 📌 Key Learnings
- Handling imbalanced data using class weights  
- Difference between ML and DL approaches  
- Importance of preprocessing for model performance  
- Understanding evaluation metrics in classification  

---

## 📷 Output
(Add screenshots here: confusion matrix / accuracy graph)

---

## 🚀 Future Improvements
- Hyperparameter tuning  
- Use of advanced models (XGBoost, CNNs)  
- Better feature engineering  

---

## 📎 Note
This project focuses on model comparison and evaluation rather than real-time prediction input.

---

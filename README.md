🌱 Soil Health Prediction using Machine Learning

This project uses Python and  Machine Learning to predict soil health based on soil test parameters such as **pH, moisture, nitrogen, phosphorus, and potassium**.  
It applies a Random Forest Classifier to classify soil as either Good or Poor  



 📌 Features
- Load soil dataset (`soil_data.csv`) using pandas
- Train a Random Forest Classifier with scikit-learn
- Evaluate the model accuracy
- Save the trained model with joblib
- Take user input to predict soil health in real-time


🗂 Dataset Example
pH,moisture,nitrogen,phosphorus,potassium,soil_health
6.5,40,50,30,20,Good
5.8,60,20,15,10,Poor
7.0,35,45,25,30,Good
4.5,70,15,10,5,Poor
6.8,50,40,20,25,Good

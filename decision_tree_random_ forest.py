import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score


#data
x=np.array([[0,1,2],[2,3,4],[4,5,6],[6,7,8],[8,9,10],[11,12,13],[13,14,15],[15,16,17],[17,18,19],[19,20,21]])
y=np.array([3,9,15,21,27,36,42,48,54,60])

x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2)

model_1 = RandomForestRegressor()
model_1.fit(x_train,y_train)

#predictt the past values
y_prediction1 = model_1.predict(x_test)

print("prediction based on the past data Random forest:",y_prediction1)
print("Random forest past outputs:",y_test)
print("accuracy of the model:\n")

print("Random forest mean_squared_error:",mean_squared_error(y_test,y_prediction1))
print("Random forest mean_absolute_error:",mean_absolute_error(y_test,y_prediction1))
print("Random forest r2_score:",r2_score(y_test,y_prediction1),"\n")


#model two
model_2 = DecisionTreeRegressor()
model_2.fit(x_train,y_train)

#predict the past values
y_prediction_2 = model_2.predict(x_test)

print("Prediction based on the past data Decision Tree:",y_prediction_2)
print("Decision Tree Regressor past outputs:",y_test)
print("accuracy of the model Decision Tree :\n")

print("Decision Tree  mean_squared_error:",mean_squared_error(y_test,y_prediction_2))
print("Decision Tree mean_absolute_error:",mean_absolute_error(y_test,y_prediction_2))
print("Decision Tree r2_score:",r2_score(y_test,y_prediction_2),"\n")
#model two
model_3 = LinearRegression()
model_3.fit(x_train,y_train)

#predictt the past values
y_prediction_3 = model_3.predict(x_test)

print("Prediction based on the past data Linear Regression :",y_prediction_3)
print("LinearRegression past outputs:",y_test)
print("accuracy of the model LinearRegression:\n")

print("Linear Regression mean_squared_error:",mean_squared_error(y_test,y_prediction_3))
print("Linear Regression mean_absolute_error:",mean_absolute_error(y_test,y_prediction_3))
print("Linear Regression r2_score:",r2_score(y_test,y_prediction_3),"\n")

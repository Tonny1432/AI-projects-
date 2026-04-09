import torch
from torch.utils.data import Dataset,DataLoader,TensorDataset
import matplotlib.pyplot as mat
from torch import nn
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
from torch import optim
from sklearn.ensemble import RandomForestClassifier

class MyDataset(Dataset):
    """Some Information about MyDataset"""
    def __init__(self):
        df = pd.read_csv("bank-additional-full-1.csv",sep=";")

        df = df.drop_duplicates()

        df = df.dropna()

        num_df = df.select_dtypes(include=['int64', 'float64'])
        q1 =num_df.quantile(0.25)
        q3 =num_df.quantile(0.75)
        iqr = q3-q1
        lower =  q1-1.5*iqr
        upper = q3+1.5*iqr
        df = df[~((num_df<lower)|(num_df > upper)).any(axis=1)]

        le = LabelEncoder()

        for columns in df.columns[:-1]:
            if df[columns].dtypes == "object":
                df[columns] = le.fit_transform(df[columns])
        
        df['y'] = df['y'].map({'no': 0, 'yes': 1})
        df = df.dropna(subset=['y'])

        self.xdl = df.iloc[:,:-1].values
        self.ydl = df.iloc[:,-1].values


    def __len__(self):
        return len(self.xdl)
    
    def __getitem__(self, idx):
         return self.xdl[idx], self.ydl[idx]
    
mydataset = MyDataset()

x = mydataset.xdl
y = mydataset.ydl

xd_train,xd_test,yd_train,yd_test = train_test_split(x,y,test_size=0.2)

xd_train = torch.tensor(xd_train, dtype =torch.float32)
xd_test = torch.tensor(xd_test, dtype =torch.float32)
yd_train = torch.tensor(yd_train, dtype =torch.long)
yd_test = torch.tensor(yd_test, dtype = torch.long)

train_data =TensorDataset(xd_train, yd_train)
test_data = TensorDataset(xd_test, yd_test)

train_loader = DataLoader(train_data,batch_size=64, shuffle=True)
model = nn.Sequential(
    nn.Linear(xd_train.shape[1],32),
    nn.ReLU(),
    nn.Linear(32,16),
    nn.ReLU(),
    nn.Linear(16,8),
    nn.ReLU(),
    nn.Linear(8,2)
)
# training the data
class_weights = torch.tensor([1.0,10])
loss = nn.CrossEntropyLoss(weight=class_weights)
optimizer= optim.Adam(model.parameters(),lr=0.017)
for i in range(50):
    for x_batch,y_batch in train_loader:
        preditions = model(x_batch)
        loss_fn = loss(preditions,y_batch)
        optimizer.zero_grad()
        loss_fn.backward()
        optimizer.step()

#testing the data
all_preds = []
all_labels = []
total =0
correct=0
test_loader = DataLoader(test_data,batch_size=64,shuffle=True)
with torch.no_grad():
    for x_batch,y_batch in test_loader:
        predict = model(x_batch)
        _,max_value = torch.max(predict,1)
        all_preds.extend(max_value.numpy())
        all_labels.extend(y_batch.numpy())
        total += y_batch.size(0)
        correct += (max_value==y_batch).sum().item()
accuracy_dl = accuracy_score(all_labels,all_preds)*100

print("accuracy of the neural network:",(correct/total) * 100)
print("accuracy of deep learning neural network accuracy score:",accuracy_dl)
print("Deep learning neural network confusion matrix:\n",confusion_matrix(all_labels,all_preds))
print("Deep learning neural network classification report:\n",classification_report(all_labels,all_preds))




model_2 = RandomForestClassifier()
model_2.fit(xd_train.numpy(),yd_train.numpy())
y_preditctions = model_2.predict(xd_test.numpy())

accuracy_ml = accuracy_score(yd_test,y_preditctions)*100

print("accuracy of Random forest classifier accuracy score:",accuracy_ml)
print("Random forest classifier confusion matrix:\n",confusion_matrix(yd_test.numpy(),y_preditctions))
print("Random forest classifier confusion matrix:\n",classification_report(yd_test.numpy(),y_preditctions))


import matplotlib.pyplot as mat

# values
models = ["Deep Learning", "Random Forest"]
accuracies = [accuracy_dl, accuracy_ml]

# graph
mat.bar(models, accuracies, color =["red","blue"])

mat.xlabel("Models")
mat.ylabel("Accuracy (%)")
mat.title("Model Comparison")

# set range 0–100
mat.ylim(0, 100)

mat.show()
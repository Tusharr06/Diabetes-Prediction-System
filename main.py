
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from trove_classifiers import classifiers

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

diabetes_dataset = pd.read_csv("/home/tushar/Documents/MLPROJECT-1/diabetes.csv")

print(diabetes_dataset.head())
print(diabetes_dataset.describe())
print(diabetes_dataset["Outcome"].value_counts())
print(diabetes_dataset.groupby("Outcome").mean())
X = diabetes_dataset.drop(columns = "Outcome",axis=1)
Y = diabetes_dataset["Outcome"]
print(X)
print(Y)
scaler = StandardScaler()
standarized_data = scaler.fit_transform(X)
print(standarized_data)
X = standarized_data
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=.2,stratify=Y,random_state=2)
classifier = svm.SVC(kernel="linear")
classifier.fit(X_train,Y_train)

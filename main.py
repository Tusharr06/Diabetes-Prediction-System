
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score


pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


#Enter the file path accordingly#
diabetes_dataset = pd.read_csv("diabetes.csv")

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
X_train_prediction = classifier.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction,Y_train)
print(training_data_accuracy)
X_test_prediction = classifier.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction,Y_test)
print(test_data_accuracy)

pregnancies = float(input("Enter number of pregnancies: "))
glucose = float(input("Enter glucose level: "))
blood_pressure = float(input("Enter blood pressure: "))
skin_thickness = float(input("Enter skin thickness: "))
insulin = float(input("Enter insulin level: "))
bmi = float(input("Enter BMI: "))
dpf = float(input("Enter Diabetes Pedigree Function: "))
age = float(input("Enter age: "))

predict_data = (pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age)

predict_data_np = np.asarray(predict_data).reshape(1, -1)

standarized_data_predict_data = scaler.transform(predict_data_np)

prediction = classifier.predict(standarized_data_predict_data)

if prediction[0] == 0:
    print("The Person Is Not Diabetic")
else:
    print("The Person Is Diabetic")



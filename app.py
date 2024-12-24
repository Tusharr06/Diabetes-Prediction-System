from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn import svm

app = Flask(__name__)

# Load the dataset
diabetes_dataset = pd.read_csv(r"C:\codes\Diabetes-Prediction-System\diabetes.csv")

# Prepare the data
X = diabetes_dataset.drop(columns="Outcome", axis=1)
Y = diabetes_dataset["Outcome"]

# Standardize the data
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train the classifier
classifier = svm.SVC(kernel="linear")
classifier.fit(X, Y)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        print("Received data:", data) 
        predict_data = np.array([data['pregnancies'], data['glucose'], data['bloodPressure'], data['skinThickness'], data['insulin'], data['bmi'], data['dpf'], data['age']]).reshape(1, -1)
        print("Predict data:", predict_data)  
        standarized_data_predict_data = scaler.transform(predict_data)
        print("Standardized data:", standarized_data_predict_data)  
        prediction = classifier.predict(standarized_data_predict_data)
        print("Prediction:", prediction) 
        result = "The Person Is Diabetic" if prediction[0] == 1 else "The Person Is Not Diabetic"
        return jsonify(result=result)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify(result="An error occurred"), 500

if __name__ == '__main__':
    app.run(debug=True)

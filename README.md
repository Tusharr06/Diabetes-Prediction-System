```markdown
# Diabetes Prediction Model

This is a **Diabetes Prediction System** built using machine learning algorithms. The model predicts whether a person is diabetic or not based on various health-related features such as glucose level, BMI, blood pressure, etc. It uses the **Support Vector Machine (SVM)** algorithm for classification and allows for interactive predictions based on user input.

## Features

- **Diabetes Prediction**: Predicts whether a person is diabetic or not based on user input.
- **Interactive User Input**: Allows users to provide data such as glucose levels, BMI, blood pressure, etc., for real-time predictions.
- **SVM Classifier**: The model is built using a Support Vector Machine classifier.
- **Model Evaluation**: The model’s accuracy is evaluated on both training and test datasets.

## Technologies Used

- **Python 3.x**: Programming language.
- **scikit-learn**: For building and evaluating the machine learning model.
- **pandas**: For data manipulation and handling the dataset.
- **numpy**: For numerical operations.
- **StandardScaler**: For standardizing the input features.

## Installation

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip (Python package installer)

### Steps to Run Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Tusharr06/Diabetes-Prediction-System
   cd Diabetes-Prediction-System
   ```

2. **Install Dependencies**:
   Install the required Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, you can install the dependencies manually:
   ```bash
   pip install pandas numpy scikit-learn
   ```

3. **Run the Application**:
   Execute the Python script:
   ```bash
   python main.py
   ```

4. **Enter User Data**:
   The system will prompt you to enter the following health-related information:
   - Number of pregnancies
   - Glucose level
   - Blood pressure
   - Skin thickness
   - Insulin level
   - BMI (Body Mass Index)
   - Diabetes Pedigree Function (DPF)
   - Age

5. **Get the Prediction**:
   After entering the data, the model will predict whether the person is diabetic or not.

## Example

Here’s an example of how the input and output look:

```
Enter number of pregnancies: 6
Enter glucose level: 125
Enter blood pressure: 68
Enter skin thickness: 30
Enter insulin level: 120
Enter BMI: 30
Enter Diabetes Pedigree Function: 0.464
Enter age: 32

The Person Is Diabetic
```
## Contributing

Feel free to fork the repository and submit pull requests if you'd like to contribute to the project. To contribute, follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Commit your changes
4. Push to your forked repository
5. Open a pull request to the main repository


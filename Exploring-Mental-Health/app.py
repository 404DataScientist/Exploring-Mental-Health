from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model pipeline
model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('form.html')

import pandas as pd

@app.route('/predict', methods=['POST'])
def predict():
    input_data = {
        'Gender': [request.form['Gender']],
        'Working Professional or Student': [request.form['Working Professional or Student']],
        'Have you ever had suicidal thoughts ?': [request.form['Have you ever had suicidal thoughts ?']],
        'Family History of Mental Illness': [request.form['Family History of Mental Illness']],
        'Dietary Habits': [request.form['Dietary Habits']],
        'FieldOfStudy': [request.form['FieldOfStudy']],
        'ProfessionalField': [request.form['ProfessionalField']],
        'SleepScore': [request.form['SleepScore']],
        'Academic Pressure': [float(request.form['Academic Pressure'])],
        'Work Pressure': [float(request.form['Work Pressure'])],
        'CGPA': [float(request.form['CGPA'])],
        'Study Satisfaction': [float(request.form['Study Satisfaction'])],
        'Job Satisfaction': [float(request.form['Job Satisfaction'])]
    }

    # Create DataFrame in the same structure as training data
    features_df = pd.DataFrame(input_data)

    # Predict
    prediction = model.predict(features_df)[0]

    return render_template('result.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)

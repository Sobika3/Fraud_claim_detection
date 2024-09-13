import os
import pandas as pd
from flask import Flask, request, render_template
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
import numpy as np

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_file_path = os.path.join(BASE_DIR, 'dataset.csv') 

data = pd.read_csv(csv_file_path)

data.ffill(inplace=True)

label_encoders = {}
categorical_cols = ['Gender', 'IsInternational']

for col in categorical_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

X = data[['Amount', 'Gender', 'Age', 'IsInternational']] 

model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
model.fit(X)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_data = {
            'Amount': float(request.form['Amount']),
            'Gender': 1 if request.form['Gender'].lower() == 'female' else 0,
            'Age': float(request.form['Age']),
            'IsInternational': 1 if request.form['IsInternational'].lower() == 'yes' else 0
        }
        input_df = pd.DataFrame([input_data])
        
        prediction = model.predict(input_df)
        prediction = np.where(prediction == -1, 1, 0)
        
        result = "Fraudulent" if prediction[0] == 1 else "Not Fraudulent"
        return render_template('index.html', result=result)
    
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)

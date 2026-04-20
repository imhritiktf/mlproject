from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd

from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.utils import save_object, evaluate_models  

app = Flask(__name__)

# rouute for home page
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/predictdata', methods=['POST','GET'])
def predict_datapoint():
    if request.method == 'GET':
       return render_template('home.html')
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('race_ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=request.form.get('reading_score'),
            writing_score=request.form.get('writing_score')
        )
        pred_df = data.get_data_as_dataframe()
        print(pred_df)

        predict_pipeline = PredictPipeline()

        result = predict_pipeline.predict(pred_df)
        return render_template('home.html', results=round(result[0], 2))
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
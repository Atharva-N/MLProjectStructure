import numpy as np
import pandas as pd
import bentoml
from bentoml.io import JSON
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

best_runner = bentoml.sklearn.get("best_model:latest").to_runner()

svc = bentoml.Service("student_performance_predictor", runners=[best_runner])

@svc.api(input=JSON(), output=JSON())
def predict(input_data: list) -> dict:
    try:
        # Extract values from input list
        gender, race_ethnicity, parental_education, lunch, test_prep, reading, writing = input_data[0]
        
        # Create CustomData instance exactly as in Flask app
        data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_education,
            lunch=lunch,
            test_preparation_course=test_prep,
            reading_score=float(reading),  # Match Flask app's conversion
            writing_score=float(writing)   # Match Flask app's conversion
        )
        
        # Get DataFrame exactly as in Flask app
        pred_df = data.get_data_as_data_frame()
        print("Input DataFrame:", pred_df)  # Add this for debugging
        
        # Use the same prediction pipeline as Flask app
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        
        return {"prediction": float(results[0])}
        
    except Exception as e:
        return {"error": str(e)}
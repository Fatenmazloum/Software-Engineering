from pydantic import BaseModel

class PredictRequest(BaseModel):
       input_data: list[float]  # List of 4 float values representing the features
    
class PredictionSchema(BaseModel):
       prediction:float
         # Assuming the prediction is a string (e.g., class label)
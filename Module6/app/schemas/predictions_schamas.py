from pydantic import BaseModel, Field
class Prediction(BaseModel):
    text: str 
    sentiment: str 

    class Config:
        orm_mode = True

class PredictionCreate(BaseModel):
    text: str

    class Config:
        orm_mode = True
   
from fastapi import APIRouter, HTTPException
from app.services.ml_services import predict, train_model
from app.utils.exceptions import invalidInputError
from app.utils.logger import get_logger
from app.schemas.ml_schemas import PredictRequest, PredictionSchema

router = APIRouter(prefix="/ml", tags=["Machine Learning"])
logger = get_logger(__name__)

@router.post("/train")
def train_model_route():
    try:
        logger.info("Starting model training.")
        train_model()
        logger.info("Model training completed successfully.")
        return {"message": "Model trained successfully."}
    except Exception as e:
        logger.error(f"An error occurred while training the model: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/predict",response_model=PredictionSchema)
def predict_route(request: PredictRequest):
    try:
        prediction = predict(request.input_data)
        if prediction is None:
            raise HTTPException(status_code=500, detail="Prediction failed.")
        logger.info(f"Prediction: {prediction}")
        return {"prediction": prediction}  # Convert numpy array to list for JSON serialization
    except invalidInputError as e:
        logger.error(f"Invalid input: {e.message}")
        raise HTTPException(status_code=400, detail=e.message)
    except Exception as e:
        logger.error(f"An error occurred during prediction: {e}")
        raise HTTPException(status_code=500, detail=str(e))

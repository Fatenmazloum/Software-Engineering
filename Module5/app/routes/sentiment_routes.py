from fastapi import APIRouter, HTTPException, Depends
from app.schemas.predictions_schamas import Prediction, PredictionCreate
from app.services.sentiment_services import predict_sentiment
from app.utils.exceptions import SentimentPipelineError, PredictionFailed
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.predictions_model import Predictions



router = APIRouter(prefix="/sentiment", tags=["Sentiment Analysis"])

@router.post("/predict-sentiment", response_model=Prediction)
def predict_sentiment_route(text: PredictionCreate, db: Session = Depends(get_db)):
    try:
        result = predict_sentiment(text.text)
        # Handle both dict and string return types
        sentiment = result['label'] if isinstance(result, dict) and 'label' in result else result
        db_prediction_item=Predictions(text=text.text, prediction=sentiment)
        db.add(db_prediction_item)
        db.commit()
        db.refresh(db_prediction_item)
        return {"text": text.text, "sentiment": sentiment}
    except SentimentPipelineError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except PredictionFailed as e:
        raise HTTPException(status_code=500, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[Prediction])
def get_all_predictions(db: Session = Depends(get_db)):
    predictions = db.query(Predictions).all()
    return [{"text": p.text, "sentiment": p.prediction} for p in predictions]

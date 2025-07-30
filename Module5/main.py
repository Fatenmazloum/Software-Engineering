from fastapi import FastAPI
from fastapi import HTTPException
from app.utils.exceptions import invalidInputError
from app.utils.logger import get_logger
from app.routes.crud_routes import router as crud_router
from app.routes.ml_routes import router as ml_router
from app.database import Base,engine
from app.models.item_model import Item
from app.routes.sentiment_routes import router as sentiment_router

#Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
 # Create tables in the database

logger=get_logger(__name__)
logger.info("Starting the model training and prediction process.")

app= FastAPI(title="Iris Flower Prediction API")
app.include_router(crud_router)
app.include_router(ml_router)
app.include_router(sentiment_router)

@app.get("/")#route definition where / is the route that is called when you go to the root URL of your API
def read_root():
    return {"message": "Welcome to the Iris Flower Prediction API!"}

@app.get("/health")
def read_root():
    return {"message": "Welcome !"}
@app.post("/name")
def name(name: str):
    if not name:
        raise HTTPException(status_code=400, detail="Name cannot be empty.")
    return {"message": f"Name '{name}' created successfully!"}

#uvicorn main:app --reload
#main = your Python file name without .py
#app = the FastAPI instance inside main.py
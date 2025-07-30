from app.services.train_model import train_model
from app.services.predict import predict
from app.utils.exceptions import invalidInputError
from app.utils.logger import get_logger

logger=get_logger(__name__)
logger.info("Starting the model training and prediction process.")

train_model()
#sepal length, sepal width, petal length, petal width
try:
    inputdata=[5.1, 3.5, 1.4]
    logger.debug(f"Input data for prediction: {inputdata}")
    prediction = predict(inputdata)
    logger.info(f"Prediction: {prediction}")
except invalidInputError as e:
    logger.error(f"Invalid input: {e.message}")

 #Importing is like saying: Bring me the tool named predict from the toolbox (predict.py).”
 # Calling the function is like saying: “Now actually use the tool to do something.”



MODEL_PATH="app/models/iris_model.pkl"
from app.utils.exceptions import invalidInputError
from app.utils.logger import get_logger
logger = get_logger(__name__)
import joblib #to save and load the model
def load_model():
    try:
        # Load the model from the specified path
        model = joblib.load(MODEL_PATH)
        return model
    except FileNotFoundError:
        logger.error(f"Model file not found at {MODEL_PATH}. Please train the model first.")
    except Exception as e:
        logger.error(f"An error occurred while loading the model: {e}")

def predict(input_data):
    if len(input_data) != 4:
        logger.error("Input data must contain exactly 4 features: sepal length, sepal width, petal length, petal width.")
        raise invalidInputError("Input data must contain exactly 4 features: sepal length, sepal width, petal length, petal width.")#call except and take message with it and after raise code stop executed
#Inside predict, it sees the mistake and raises an error.
#The error jumps back to your main code where you have try and except.
#The except catches the error and lets you handle it (like showing a message).
#Your program doesn’t crash and keeps running.

        # Load the trained model
    model = load_model()
        # Make predictions
    try:
        prediction = model.predict([input_data])
        return prediction

    except Exception as e:
        logger.error(f"An error occurred during prediction: {e}")
        return None
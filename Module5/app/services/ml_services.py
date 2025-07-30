from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from app.utils.logger import get_logger
import os
import joblib #to save and load the model
from app.utils.exceptions import invalidInputError

MODEL_PATH="app/models/iris_model.pkl"
logger = get_logger(__name__)


def train_model():
    try: 
        # Load dataset
        iris = load_iris()
        X = iris.data
        y = iris.target

        # Split dataset
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train model
        model = RandomForestClassifier()
        model.fit(X_train, y_train)

    # Save model
        joblib.dump(model, MODEL_PATH)

    except Exception as e:
        logger.error(f"An error occurred while training the model: {e}")


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
        #continue exceution but record the problem
        logger.error("Input data must contain exactly 4 features: sepal length, sepal width, petal length, petal width.")
        #stop the execution and raise an error
        raise invalidInputError("Input data must contain exactly 4 features: sepal length, sepal width, petal length, petal width.")#call except and take message with it and after raise code stop executed
  
        # Load the trained model
    model = load_model()
        # Make predictions
    try:
        prediction = model.predict([input_data])
        return prediction

    except Exception as e:
        logger.error(f"An error occurred during prediction: {e}")
        return None
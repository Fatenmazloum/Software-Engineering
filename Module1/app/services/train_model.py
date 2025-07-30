from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from app.utils.logger import get_logger
import joblib
import os

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
        joblib.dump(model, os.path.join("app/models", "iris_model.pkl"))

    except Exception as e:
        logger.error(f"An error occurred while training the model: {e}")
    
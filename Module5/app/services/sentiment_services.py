from transformers import pipeline
from app.utils.logger import get_logger
import re # Regex module for text preprocessing
from app.utils.exceptions import SentimentPipelineError, PredictionFailed


logging = get_logger(__name__)
try:
    sentiment_pipeline = pipeline("sentiment-analysis")
except Exception as e:
    logging.error(f"Error loading sentiment analysis pipeline: {e}")
    sentiment_pipeline=None
    raise SentimentPipelineError("Failed to load sentiment analysis pipeline. Check the logs for details.")#raise an error in order to stop the execution of the code if the pipeline fails to load

#preprocessing
def preprocess_text(text: str) -> str:
    """
    Preprocess the input text by removing unnecessary characters and formatting.
    """
    if not text:
        raise ValueError("Input text cannot be empty.")
    
    # Example preprocessing: remove extra spaces and convert to lowercase
    #text = "   Hello   world \n", text.split()  ➝ ['Hello', 'world'], ' '.join(...) ----> " Hello world \n" becomes "Hello world"
    #strip() removes only outer spaces, but not inner spaces like split() does
    processed_text = ' '.join(text.split()).lower()
    #remove special characters, punctuation, etc. if needed
    processed_text = re.sub(r'[^\w\s]', '', processed_text)  # Example regex to remove punctuation
    #remove https links
    processed_text = re.sub(r'http\S+|www\S+|https\S+', '', processed_text, flags=re.MULTILINE)
    return processed_text

def predict_sentiment(text: str) -> dict:
    """
    Predict the sentiment of the input text.
    """
    if not sentiment_pipeline:
        raise SentimentPipelineError("Sentiment analysis pipeline is not initialized.")
    
    # Preprocess the text
    processed_text = preprocess_text(text)
    
    # Predict sentiment
    try:
        result = sentiment_pipeline(processed_text)
        return result[0]  # Return the first prediction result
    except Exception as e:
        logging.error(f"Error during sentiment prediction: {e}")
        raise PredictionFailed("Failed to predict sentiment. Check the logs for details.")
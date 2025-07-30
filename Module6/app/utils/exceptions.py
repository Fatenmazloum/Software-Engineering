 #build exceptions in utils.exceptions, Keep your code cleaner, Avoid repeating error-handling logic, Improve readability and debugging
class invalidInputError(Exception):
    """Exception raised for invalid input data."""
    def __init__(self, message="Invalid input data provided."):#called when raising the exception
        self.message = message
        super().__init__(self.message)#passes the message to the base Exception 

#defining your own error type to use in your code instead of using only generic ones like ValueError.

class itemNotFoundError(Exception):
    """Exception raised when an item is not found."""
    def __init__(self, message="Item not found."):
        self.message = message
        super().__init__(self.message)

class SentimentPipelineError(Exception):
    """Exception raised for errors in sentiment analysis."""
    def __init__(self, message="Sentiment analysis failed."):
        self.message = message
        super().__init__(self.message)
        
class PredictionFailed(Exception):
    """Exception raised when sentiment prediction fails."""
    def __init__(self, message="Sentiment prediction failed."):
        self.message = message
        super().__init__(self.message)
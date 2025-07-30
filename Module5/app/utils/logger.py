import logging#recording important messages about your program while it's running.(track what's happening,debug problems,monitor usage or errors.)
import os
def get_logger(name):
    """
    Create a logger with the specified name.
    
    Args:
        name (str): The name of the logger.
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)#creates a logger object with the specified name
    logger.setLevel(logging.DEBUG)  # I want to see all messages with level DEBUG and above (INFO, WARNING, ERROR, CRITICAL).
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')#format of the log messages
    # Create console handler and set level to debug
    os.makedirs("logs", exist_ok=True)  # Ensure the models directory exists
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)#set the format for the console handler
    logger.addHandler(ch)#add the console handler to the logger

    #file handler to save logs to a file
    fh = logging.FileHandler('logs/app.log')#creates a file handler that writes log messages
    fh.setFormatter(formatter)#set the format for the file handler
    logger.addHandler(fh)#add the file handler to the logger

    return logger#returns the configured logger instance so you can use it in your code
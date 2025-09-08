import logging
import sys

def setup_logger():
    
    #Setting up the logger
    logger = logging.getLogger('BinanceBot')
    logger.setLevel(logging.INFO)

    logger.propagate = False      #prevention of log propagation in root folder

    #Ensure the avoidance of logs duplication
    if logger.hasHandlers():
        logger.handlers.clear()

    #file handler for bot.log
    file_handler = logging.FileHandler('bot.log')
    file_handler.setLevel(logging.INFO)

    #setup console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    #establishing format
    format = logging.Formatter('%(asctime)s - %(levelname)s - %(msg)s')

    #assigning format to file and console handler
    file_handler.setFormatter(format)
    console_handler.setFormatter(format)

    #adding handlers to loggers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

#LOGGER INITIALISED
log = setup_logger()
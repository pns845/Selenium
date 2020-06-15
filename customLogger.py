import inspect
import logging

def custom_Logger(logLevel=logging.DEBUG):
    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("automation.log",mode="w")
    fileHandler.setLevel(logLevel)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p' )
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger
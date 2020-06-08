import logging

class LoggerConsole():
    def test(self):
        #Create loggers
        logger = logging.getLogger(LoggerConsole.__name__)
        #create handlers
        c_handler = logging.StreamHandler()
        c_handler.setLevel(logging.INFO)#set level
        f_handler = logging.FileHandler('testfile.log')
        f_handler.setLevel(logging.ERROR)
        #create formators
        c_format = logging.Formatter('%(asctime)s,%(name)s,%(message)s',datefmt='%d/%m/%Y %I%M%S %p')
        f_format = logging.Formatter('%(asctime)s,%(name)s,%(message)s',datefmt='%d/%m/%Y %H%M%S %p')
        #Adding formators to handlers
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        #adding handlers to logger
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)

        logger.debug("this is debug and will not print in both")
        logger.info("this is info and prints on console")
        logger.warning("this is warning and prints in console")
        logger.error("this is error and prints in both")

lc=LoggerConsole()
lc.test()





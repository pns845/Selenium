#debug
#info
#warning
#error
#critical
#by default the logging module logs the messages with a severity level of WARNING or above.
# so the info message is not displayed in text file
#default config of file is append
#The default setting in basicConfig() is to set the logger to write to the console in the following format:

import logging
logging.basicConfig(filename="testing.txt",level=logging.DEBUG)
logging.info("testing info")
logging.warning("testing warning")
logging.error("testing error")
logging.critical("testing critical")


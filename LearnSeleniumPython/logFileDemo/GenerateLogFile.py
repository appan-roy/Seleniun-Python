import logging

# log file config
logging.basicConfig(filename = "..//Logs//Test.log", format = "%(asctime)s: %(levelname)s: %(message)s",
                    datefmt = "%d/%m/%Y %I:%M:%S %p")

# create logger object
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# set log messages
logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")
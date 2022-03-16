import logging

# adding logs to file testing.log
logging.basicConfig(filename="testing.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
print(logging.__file__)

logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
 
# Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")
import logging


# Logging Levels:

# CRITICAL
# ERROR
# WARNING(Default)
# INFO
# DEBUG

logging.basicConfig(format= '%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)

logging.critical("This message is Critical")
logging.error("This message is Error")
logging.warning("This message is Warning")
logging.info("This message is Info")
logging.debug("This message is Debug")



import logging

class Logger_demo_consol():

    def testlog(self):

        # Create formatter
        formatter = logging.Formatter('%(asctime)s under %(name)s : %(levelname)s : %(message)s', datefmt='Year :%Y  %d/%m at %I:%M:%S %p ')

        # Create Handler (Console handler) and set level
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.ERROR)
        chandler.setFormatter(formatter)

        # Create Logger and set level
        logger = logging.getLogger(Logger_demo_consol.__name__)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(chandler)

        # Messages to log
        logger.critical("This message is Critical")
        logger.error("This message is Error")
        logger.warning("This message is Warning")
        logger.info("This message is Info")
        logger.debug("This message is Debug")


test = Logger_demo_consol()
test.testlog()
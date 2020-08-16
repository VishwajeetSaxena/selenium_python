import logging
import logging.config

class LoggerDemoConf():

    def testLog(self):
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggerDemoConf.__name__)

        # logging messages
        logger.debug('debug message')
        logger.info('info message')
        logger.error('error message')
        logger.critical('critical message')

temp = LoggerDemoConf()
temp.testLog()
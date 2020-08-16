import logging
from custom_logger_package import custom_logger as cl


class SampleClass1():

    log = cl.customLogger(logging.INFO)

    def method1(self):
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method2(self):
        method_Log = cl.customLogger(logging.INFO)
        method_Log.debug('debug message')
        method_Log.info('info message')
        method_Log.error('error message')
        method_Log.critical('critical message')

    def method3(self):

        self.log.debug('debug message')
        self.log.info('info message')
        self.log.error('error message')
        self.log.critical('critical message')

temp = SampleClass1()

temp.method1()
temp.method2()
temp.method3()
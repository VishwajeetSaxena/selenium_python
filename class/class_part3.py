#Global variable
my_global_variable = 55
class SampleClass3(object):

    def __init__(self, value1 ,value2, value3):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3

    def sampleMethod1(self):
        global my_global_variable
        my_global_variable = 99
        print('....inside method 1', my_global_variable)

    def sampleMethod2(self):
        global my_global_variable
        #Global variable value can be passed from one method to other
        print('....inside method 2', my_global_variable)


# To Access and Change the value of global variable
obj1 = SampleClass3(1,33,43)
print('My Global variable before change by method#1', my_global_variable)
obj1.sampleMethod1()
print('My Global variable after change by method#1', my_global_variable)
obj1.sampleMethod2()


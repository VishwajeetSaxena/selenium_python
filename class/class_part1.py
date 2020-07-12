#Sample class and it's init constructor

class SampleClass(object):

    def __init__(self, value1 ,value2, value3 = 'this is default value'):

        #Difine instance variable

        #1. taking value using outside parameter
        self.value1_of_class_variable = value1

        #2. taking value using outside parameter and assigned to same name variable, which is common practice
        self.value2 = value2

        #3. taking default value
        self.value3_of_class_variable = value3

        #Calling a class method
        self.sample_method2()

    def sample_method1(self, value4):
        print('This is just a sample method')
        print('Sum of all the the values are: ', (self.value1_of_class_variable + self.value2 + self.value3_of_class_variable + value4))

    def sample_method2(self):
        print('Just printing a somethings automatically as soon as class instance created')




#Create instance/object of class
sample_object1 = SampleClass(21,34,90)

#Get the values outside of the class
print('Value#1 is:', sample_object1.value1_of_class_variable)
print('Value#2 is:', sample_object1.value2)
print('Value#3 is:', sample_object1.value3_of_class_variable)

#Call the methods oustide of the class
print('Methods outside the class:')
sample_object1.sample_method1(100)
sample_object1.sample_method2()
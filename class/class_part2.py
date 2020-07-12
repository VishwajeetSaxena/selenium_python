#Class variable

class SampleClass2(object):

    #Member/Class/Global varaible
    my_class_variable = 10

    def __init__(self, value1 ,value2, value3):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3


obj1 = SampleClass2(1,33,43)
obj2 = SampleClass2(1,1,1)

# To distribute value between multiple instances
# Access and Change the value of class variable using class
print('My class variable using class', SampleClass2.my_class_variable)
print('                  using object 1', obj1.my_class_variable)
print('                  using object 2', obj2.my_class_variable)
SampleClass2.my_class_variable = 11
print('My class variable using class', SampleClass2.my_class_variable)
print('                  using object 1', obj1.my_class_variable)
print('                  using object 2', obj2.my_class_variable)

print('*'*20)

# To keep value between single instance
# Access and Change the value of class variable using instance
print('My class variable using class', SampleClass2.my_class_variable)
print('                  using object 1', obj1.my_class_variable)
print('                  using object 2', obj2.my_class_variable)
obj1.my_class_variable = 900
print('My class variable using class', SampleClass2.my_class_variable)
print('                  using object 1', obj1.my_class_variable)
print('                  using object 2', obj2.my_class_variable)

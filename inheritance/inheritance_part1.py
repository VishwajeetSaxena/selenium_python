class Car(object):
    material = 'Metal'

    def __init__(self):
        print('Data from super class')

    def wheel_type(self):
        print('Has four tyres')

class Duster(Car):
    material = 'Steel'
    def __init__(self):
        print('Data from child class')
        #Optional to call super constructor/method
        #1
        Car.__init__(self)
        #2
        super().__init__()

    def category_type(self):
        print('It is an SUV')

    def build_type(self):
        print('It is build of', Car.material)
        print('Specifically by', self.material)

print('*'*20)
d = Duster()
#Access super class methods
d.wheel_type()
d.category_type()

print('*'*20)
#Access super class variable
d.build_type()

print('*'*20)
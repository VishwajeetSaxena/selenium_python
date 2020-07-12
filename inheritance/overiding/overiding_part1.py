class Car(object):

    def __init__(self):
        print('Data from super class')

    def wheel_type(self):
        print('Has four tyres')

class Duster(Car):

    def __init__(self):
        print('Data from child class')

    #Overidden the parent class method
    def wheel_type(self):
        #Still able to use parent class method
        #1
        super().wheel_type()
        #2
        super(Duster, self).wheel_type()
        #Code specific to child
        print('It also has one extra tyre')


print('*'*20)
d = Duster()

#Access super class methods
d.wheel_type()

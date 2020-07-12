
#import only sqrt method from entire module
from math import sqrt

class ModulesDemo():

    def builtin_modules(self):
        #reference the sqrt method directly
        print(sqrt(100))


m = ModulesDemo()
m.builtin_modules()

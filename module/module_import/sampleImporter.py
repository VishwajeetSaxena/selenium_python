from module.module_package.samplePackage import info

class ModulesDemo():

    def car_description(self):
        make = "bmw"
        model = "550i"
        info(make, model)


m = ModulesDemo()
m.car_description()
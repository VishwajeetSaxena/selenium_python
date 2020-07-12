#Variable scope
a = 10

def variable_scope_local():
    a = 2
    print('value inside the method', a)

variable_scope_local()
print('value outside the method', a)


def variable_scope_global():
    global a
    a = 21
    print('value inside the method', a)

variable_scope_global()
print('value outside the method', a)

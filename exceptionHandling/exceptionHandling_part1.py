#Exception Handeling

#Try & Except
def exception_handeling():
    a = 12
    b = 6
    c = 0
    d = 0
    try:
        d = (a+b) / c
        print('D is: ', d)
    except ZeroDivisionError:
        print('There is ZeroDivisionError')
    except TypeError:
        print('There is TypeError')
    except:
        print('There is Error')

exception_handeling()

print('*'*40)

def exception_handeling2():
    a = 12
    b = 'Sample string'
    c = 0
    d = 0
    try:
        d = (a+b) / c
        print('D is: ', d)
    except ZeroDivisionError:
        print('There is ZeroDivisionError')
    except TypeError:
        print('There is TypeError')
    except:
        print('There is Error')

exception_handeling2()

print('*'*40)

def exception_handeling3():
    a = 12
    b = 6
    c = 0
    d = 0
    try:
        d = (a+b) / c
        print('D is: ', d)
    except:
        print('There is Error')

exception_handeling3()

print('*'*40)
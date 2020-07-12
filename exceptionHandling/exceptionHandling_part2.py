#Exception Handeling

# Else & Finally

# Else
def exception_handeling():
    a = 12
    b = 6
    c = 2
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
    else:
        print('This is executed because there is no error')
    finally:
        print('This will always execute')

exception_handeling()

print('*'*40)

# Finally
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
    else:
        print('This is executed because there is no error')
    finally:
        print('This will always execute')

exception_handeling()

print('*'*40)

#Exception Handeling

# Raise Exception
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
        raise exception_handeling()
        # raise Exception('The error is im Block#1')
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

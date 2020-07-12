#Method with parameters
def sum_num(num1, num2):
    '''
    :param num1:
    :param num2:
    :return:
    '''
    print(num1 + num2)

sum_num(2, 3)
sum_num(34, 4)
sum_num('hello', ' how are you')


#Method with return value
def sum_num_with_return(num1, num2):
    '''
    :param num1:
    :param num2:
    :return:
    '''
    return (num1 + num2)
returned_value = sum_num_with_return(45, 55)
print("The returned value is: ", returned_value)

def conditional_return(city):

    metro_cities = ['Newyork', 'Boston', 'Mumbai', 'New Delhi']
    if city in metro_cities:
        return True
    else:
        return False

city_name = 'Boston'

conditional_return_value = conditional_return(city_name)
print(city_name, 'is a metro: ', conditional_return_value)

print('Bangalore is a metro: ', conditional_return('Bangalore'))

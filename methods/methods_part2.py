#Method with positional oparameters
def sum_num(num1=1, num2=4):
  return (num1 + num2)

print('Sum with no parameter', sum_num())

print('Sum with first parameter', sum_num(num1=1))
print('Sum with first parameter', sum_num(1))
print('Sum with first parameter', sum_num(1,))

print('Sum with second parameter', sum_num(num2=1))

print('Sum with all parameters', sum_num(num1=3, num2=1))
print('Sum with all parameters', sum_num(3, 1))

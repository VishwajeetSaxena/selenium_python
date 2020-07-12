#Method with changable length of parameters
def method_with_args(*args):
  i = 0
  total = 0

  for i in args:
   total = total + i

  return total

print(method_with_args(4,8))
print(method_with_args(4,56,8))

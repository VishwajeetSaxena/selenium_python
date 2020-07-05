# AND operator
# value1 = 2 and 1
value1 = 2 and (10 == 10)
print("Result of AND operation, on first and second value is", value1)

# OR operator
value2 = 1 or 1
print("Result of OR operation, on first and second value is", value2)

# NOT operator
# value3 = not(1)
value3 = not(10 == 11)
print("Result of NOT operation on, a value is", value3)

#Precedancy is :
#1. Not (Highest)
#2. AND
#3. OR
value4 = True or not False and True
#above will be treated as value4 = True or ((not False) and True)
print("The value based on the expression is", value4)

# #Break
list1 = []
x = 0
while x < 20:
    if x == 17:
        break #broke the while loop when x is equal to 17, no further iteration

    list1.append(2*x)
    x = x + 1

print(list1)

#Continue

list2 = []
y = 0
while y < 20:
    y = y + 1
    if y == 17:
        continue #skip the remaining statement in the loop when x is equal to 17, and proceed for further iteration
        print("hi")
    list2.append(2*y)
print(list2)

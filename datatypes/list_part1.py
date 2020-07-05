#list of strings
list1 = ["abc", "def","ghi"]
#list of numbers
list2 = [1,2,3]

#fetch value from a particular list index
print(list1[0])
print(list2[2])

'''
List is mutable unlike string
We can change value of a particular item of list
'''
print("Before reassignment :", list1)
list1[1] = "xyz"
print("After reassignment :", list1)

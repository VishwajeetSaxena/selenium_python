#Strings are immutable

'''
Changing the particular string item(character) is not possible
we can only reassign a new value to complete string(string1 = "def"), while doing so..python will remove string1 pointer from previous location(where "abc" saved) and point to new location where "def" saved.
Later it will delete the unreferenced data location automatically
'''
string1 = "abc"
string1[1] = "d" #This line will give error


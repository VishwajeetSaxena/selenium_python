string1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Get the sub-string from starting index to ending index
print("Get the sub-string from starting index to ending index: ", string1[1:20])


#Get the sub-string from starting index to ending index with step count 2
print("Get the sub-string from starting index to ending index with step count 2: ", string1[1:20:2])

#No starting index to ending index
print("No starting index to ending index: ", string1[:])

#No starting index to ending index
print("No ending index: ", string1[3:])

#No starting index to ending index
print("No starting index: ", string1[:6])

#No starting index to ending index , just step count
print("No starting index to ending index , just step count: ", string1[::2])

#Negative start index
print("Negative start index:", string1[-1])

#Negative end index
print("Negative end index:", string1[:-1])

'''
This also useful to reverse string
'''
#Negative step
print("Negative step:", string1[::-1])


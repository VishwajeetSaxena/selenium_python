#Access specific character of string
string1 = "This is sample string"
string2 = string1[3]
print("full string:", string1,"with type: ", type(string1))
print("specific character of string: ", string2, "with type: ", type(string2))

#Get length of string
print("Length of string is: ", len(string1))

#Get lower case data of string
print("The lower case of the string is: ", string1.lower())

#Get uppper case data of string
print("The upper case of the string is: ", string1.upper())

#Concat the strings
string3 = "Hello"
string4 = "World"
string5 = string3+string4
print("Merged string is: ", string5)

#Replace strings
string6 = "1abc2abc3abc4abc"
print("Replace all 'abc' with 'ABC' :", string6.replace('abc', 'DEF'))
print("Replace first two 'abc' with 'ABC' :", string6.replace('abc', 'DEF', 2))

#different ways to parameterize the printed strings
print("I just want to add", string3, "in this line along with", string4)
print("I just want to add "+string3+" in this line along with "+string4)
print("I just want to add %s in this line along with %s" % (string3, string4))

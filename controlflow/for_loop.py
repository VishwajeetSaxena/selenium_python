#for loop: String
print()
string1 = "This is sample string"

for s in string1:
    print(s.upper(), end=' |')

#for loop: List
print()
list1 = ['list_item1', 'list_item2', 'list_item3', 'list_item4']

for i in list1:
    print('The fetched list item is: ', i)

#for loop: Tuple
print()
tuple1 = ('tuple_item1', 'tuple_item2', 'tuple_item3', 'tuple_item4')

for j in tuple1:
    print('The fetched tuple item is: ', j)

#for loop: Dictionary
dictionary1 = {'dict_item1': 23, 'dict_item2': 48, 'dict_item3': 'No luck', 'dict_item4': 'You Win'}
print()
print('The items in dictionary are: ', dictionary1.items())
print('The keys in dictionary are: ', dictionary1.keys())
print('The values in dictionary are: ', dictionary1.values())

#method#1
for k in dictionary1:
    print()
    print('The fetched dictionary key is: ', k)
    print('The fetched dictionary value is: ', dictionary1[k])

#method#2
for k, v in dictionary1.items():
    print()
    print('The fetched dictionary key is: ', k)
    print('The fetched dictionary value is: ', v)

#Zip the list
list1 = [1, 45, 54, 74, 23, 38]
list2 = [3, 56, 36, 94, 2]
list3 = ['A', 'B', 'C', 'D']
for a, b, c in zip(list1, list2, list3):
    print(c)
    print(a)
    print(b)


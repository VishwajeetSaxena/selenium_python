#Declare and define dictionary
dictionary1 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'}
print("Dictionary 1", dictionary1)

#Declare empty dictionary
dictionary2 = {}
print("Dictionary 2", dictionary2)

#Get the value from dictionary
print("Value is", dictionary1['key3'])

#Just like list (and unlike String) , dictionary is mutable
dictionary1['key1'] = 'new value1'
dictionary1['key6'] = 'value6'
print(dictionary1)

#Nested dictionary
dictionary2 = {'key1': {'nested_key1': 'nested_value1', 'nested_key2': 'nested_value2', 'nested_key3': 'nested_value3'}, 'key2': 'value2', 'key3': ['list_item1', 'list_item2', 'list_item3']}

print("Print value of dictionary inside a dictionary", dictionary2['key1']['nested_key2'])

print("Print value of list item inside a dictionary", dictionary2['key3'][2])

dictionary1 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'}

#get the collection of all items(keys+values)
print(dictionary1.items())

#get the collection of all keys+values
print(dictionary1.keys())

#get the collection of all values
print(dictionary1.values())

#pop a value for a particular key
print(dictionary1.pop('key2'))

#reference a dictionary
dictionary2 = dictionary1
print(dictionary2)
dictionary1.popitem()
print(dictionary1)
print(dictionary2)

#copy a dictionary
dictionary2 = dictionary1.copy()
print(dictionary2)
dictionary1.popitem()
print(dictionary1)
print(dictionary2)

#clear a dictionary
dictionary2.clear()
print(dictionary2)


list1 = ["item1", "item2", "item3", "item4"]

#Get the length(number of items) of list
print("Length of list is", len(list1))

#Append new item in the list
list1.append("item5")
print("List after append", list1)

#Insert new item at specified location
list1.insert(1, "item1.1")
print("List after insert", list1)

#Pop(Remove) and return a last/particular index item in list
popped_item = list1.pop()
print("Popped up", popped_item)
print("List after pop", list1)

popped_item = list1.pop(1)
print("Popped up another item", popped_item)
print("List after another pop", list1)

#Remove particular value item in list
popped_item = list1.remove("item3")
print("List after another remove", list1)

#Get the first index for particular item
item_index = list1.index("item2")
print("Index of the item is", item_index)

#sort the list
list2 = ["item2", "item1", "item5", "item4", "item5"]
list2.sort()
print("The sorted list is", list2)

#Get the particular item's count(number of times it exist in the list)
print("Particular item's count", list2.count("item5"))


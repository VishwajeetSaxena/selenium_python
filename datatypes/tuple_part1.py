#Tuple behave same as list , only difference is , tuple is immutable (unlike list)

#Declaring and defining of tuple be together else we can ot add anything in tupple at later stage
# list1 = ["item1", "item2", "item3", "item4"]
tuple1 = ("item1", "item2", "item3", "item4", "item3")
tuple2 = ()
# list1.append("item5") #This is possible
# tuple2.append("item5") #This is not possible

#Get the length(number of items) of tuple
print("Length of list is", len(tuple1))

#Pop(Remove) and return a last/particular index item in list
print("tuple before pop", tuple1)
#popped_item = tuple1.pop() # Not possible
#print("Popped up", popped_item)
#print("tuple after pop", tuple1)

# popped_item = tuple1.pop(1) # Not possible
# print("Popped up another item", popped_item)
# print("Tuple after another pop", tuple1)

#Remove particular value item in list
# tuple1.remove("item3") # Not possible
# print("List after another remove", tuple1)

#Get the first index for particular item
item_index = tuple1.index("item2")
print("Index of the item is", item_index)

#sort the tuple
# tuple3 = ("item2", "item1", "item5", "item4", "item5")
# tuple3.sort() # Not possible
# print("The sorted tuple is", tuple3)

#Get the particular item's count(number of times it exist in the list)
print("Particular item's count", tuple1.count("item3"))


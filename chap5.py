myDict = {
    "Fast": "In a Quick Manner",
    "Rida": "A coder",
    "Marks": [3,4,4],
    "anotherDict": {'ridaa': 'coder'}
}
print(myDict['Fast'])
print(myDict['Marks'])
print(myDict['anotherDict']['ridaa'])

# Methods of Dictionary 

myDict = {
    "Fast": "In a Quick Manner",
    "Rida": "A coder",
    "Marks": [3,4,4],
    "anotherDict": {'ridaa': 'coder'},
    1 : 4
}
print(list(myDict.keys())) #Prints the keys of the dictionary
print(myDict.values()) #Prints the values of the dictionary
print(myDict.items()) #Prints the (key, values) for all contents of the dictionary
print(myDict)
updateDict = {
    "Rida11": "Student"
}
myDict.update(updateDict) #Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

# print(myDict.get("Rida9")) #Returns none as Rida9 is not present in the dictionary
# print(myDict["Rida9"])  #Both of them returns the same value but square bracket one throws an error as Rida9 is not present in the dictionary

#Sets in Python
# a = {1,2,3,4,5,1,2} #Doesnt print repititive values
# print(type(a))
# print(a)

#Empty Set
# Important: This syntax will create an empty dictionary and not an empty set 
a = {}
print(type(a))

# An empty set can be created using the below syntax:
b = set()
print(type(b))
#Adding values to an empty set
b.add(4)
b.add(9)
b.add(4) #adding the value repeatedly does not changes a set
# b.add([4, 5, 6]) List cant be added in a set
b.add((4,5,6)) #Tuple can be added in a set
print(b)

# Length of the set 
print(len(b)) #Prints the length of this set

# Removal of an Item 
b.remove(9) #Removes the mentioned item from the set
# b.remove(10) #Generates error bec 10 is not present in the set
print(b)

print(b.pop()) #Removes any item by itself from the set
print(b)

print(b.clear()) #Set becomes empty
print(b)





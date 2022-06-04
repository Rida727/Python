# Create list 
a = [5, 8, 9, 67]
a[1] = 89
print(a)

# We can create a list with items of different types 
b = [45, "rida", False, 8.99]
print(b)

# List Slicing 
friends = ["Rida", "Laiba", "Jav", "Mano", "Izma", 89]
print(friends[1:5])
print(friends[-3:])

# List Methods 

l1 = [9, 2, 6, 9, 9, 89, 27, 0]
print(l1)
# l1.sort() --> Sorts the list 
print(l1)

l2 = [9, 2, 6, 9, 9, 89, 27, 0]
print(l2)
# l2.reverse() --> reverses the list 
print(l2)

l3 = [9, 2, 6, 9, 9, 89, 27, 0]
print(l3)
# l3.append(40) --> adds at the end of the list 
print(l3)

l4 = [9, 2, 6, 9, 9, 89, 27, 0]
print(l4)
# l4.insert(0,67) --> adds 67 at 0 position 
print(l4)

l4 = [9, 2, 6, 9, 9, 89, 27, 0]
print(l4)
# l4.pop(2) --> removes the number that is at position 2
print(l4)

l4 = [9, 2, 6, 9, 9, 89, 27, 0]
print(l4)
# l4.remove(89) --> removes the number 89 from the list 
print(l4)

#Tuples
a = (1, 2, 3 ,4)
print(a)
# a[0] = 89 --> cant be update in tuples 

# Empty Tuple 
b = ()
print(b)

#Wrong way to declare a tuple with single element
b = (1)
print(b)

# Tuple with single element 
b = (8,)
print(b)

#Methods of Tuples
r = (1, 2, 3, 2, 4, 2)
# print(r.count(2)) --> how many 2 are present in a tuple 
# print(r.index(3)) --> tells the index number of given number from the tuple 


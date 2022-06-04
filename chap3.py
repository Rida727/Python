# a = "Ridaaa"
# a = 'Rida"s' --> Single Quote
# a = "Rida's" --> Double Quote
# a = '''Rida"ss''' #--> Triple Quote
# print(a)
# print(type(a))

# #Concatenating two strings
# name = "Rida, "
# department = "Software Engineering, "
# rollno = "2019-SE-089"
# print(name + department + rollno)

#String Indexing
# name = "Rida"
# print(name[0])

#String Slicing
# name = "Rida"
# print(name[0:4])
# print(name[:4]) 
# print(name[1:]) 

#Negative Indexing   ???
name1 = "Ridaz"
print(name1[-4:-1])

#Slicing with Skip Value
name = "RidaSohail"
print(name[1::5])

#String Functions
story = "my name is Rida Sohail"
print(len(story))
print(story.endswith("Sohail"))
print(story.count("a"))
print(story.capitalize())
print(story.find("is"))
print(story.replace("Rida", "Sana"))

#Escape Sequence Characters/Escape Sequences
story = "my name is rida sohail.\n i am\t fro\\m \'ssuet"
print(story)
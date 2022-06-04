#Question 1

# myDict = {
#     "Pankha": "Fan",
#     "Dabba": "Box",
#     "Subah": "Morning"
# }
# print("Options are ", myDict.keys())
# a = input("Enter the Hindi word\n")
# # print("The meaning of your word is:", myDict[a]) 

# #Below line will not throw an error if the key is not present in the dictionary
# print("The meaning of your word is:", myDict.get(a))

#Question 2

# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# num3 = int(input("Enter number 3: "))
# num4 = int(input("Enter number 4: "))
# num5 = int(input("Enter number 5: "))
# num6 = int(input("Enter number 6: "))
# num7 = int(input("Enter number 7: "))
# num8 = int(input("Enter number 8: "))

# s = {num1, num2, num3, num4, num5, num6, num7, num8}
# print(s)

#Question 3

r = {18, "18", 18.1}
print(r)

#Question 4

s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))

#Question 6

favLang = {}
a = input("Enter your fav lang rida: ")
b = input("Enter your fav lang sana: ")
c = input("Enter your fav lang faraz: ")
d = input("Enter your fav lang manno: ")
favLang["rida"] = a
favLang["sana"] = b
favLang["faraz"] = c
favLang["manno"] = d
print(favLang)


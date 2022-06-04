ridaDict = {
    "abc":"1234",
    "rs":"hello",
    "Marks":[1,2,3],
    "num":(2,3,4),
    "rida1":{'hi':'bye'}
    
    
}
print(ridaDict["abc"])
print(ridaDict["Marks"])
print(ridaDict["num"])
print(ridaDict['rida1']['hi'])
print(list(ridaDict.keys()))
print(list(ridaDict.values()))
print(list(ridaDict.items()))
updateDict = {
    "Rida45":"byeee"
}
ridaDict.update(updateDict)
print(updateDict)

#SETS

a ={1,2,2,3,3,4,5,6}
print(type(a))
print(a)

b={}
print(type(b))

c= set()
print(type(c))
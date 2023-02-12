mydict = {
    "brand":"Ford",
    "year":1908,
    "owner":"Mr. Sayak"
}

x = mydict.keys()
print(x)

#Adding another key to the dictionary
mydict["color"] = "BLUE"
print(x)

#Getting Items as a tuple
y = mydict.items()
print(y)

#LOOPING ALL THE KEYS AND VALUE PAIRS
for a,b in mydict.items():
    print(a,b)

m=mydict.setdefault("owner","Mr. Sayak")
# The setdefault() method returns the value of the item with the specified key.
print(m)

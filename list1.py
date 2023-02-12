print("This is me.")

thislist= ["apple","banana","orange"]
thislist[2:3]=["cocktail"]

tropical=["India","Delhi","Gujarat"]
thislist.extend(tropical)
# del thislist
thislist.clear()
#clear() empties the list, therefore, no values bu tlist still exists
print(thislist)

tropical202=["I","fuck","you","so much"]
tropical202.insert(1,"love")
tropical202.remove("fuck")
print(tropical202)

# Simplest way to loop 
for x in tropical202:
    print(x)

# anothere way to loop through a list 
for y in range(len(tropical202)):
    print(tropical202[y])
# Shortest syntax for a loop
[print(x) for x in tropical202]


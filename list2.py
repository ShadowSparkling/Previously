# appending from a new list 
newlist=["apple","banana","mango","cherry","lobby"]
newlist2=[]
for x in newlist:
    if "a" in x:
        newlist2.append(x)

print(newlist2)

# With List Comprehension you can do it with shorter syntax 

newlist3={x for x in newlist if "a" in x}
print(newlist3)

number=[x for x in range(10)]
print(number)

number2 = [x for x in number if x>6]
print(number2)

# Using if else in making a list 
number3=[x if x!=9 else 300 for x in number]
print(number3)

# Reversing the order of the list 
number3.sort(reverse=True)
print(number3)

#Adding two lists to make one
number4=number2+number3
number4.sort()
print(number4)
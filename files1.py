# f = open("demo.txt","r")
# print(f.read())
# print(f.read(10))
# print(f.readline())
# f.close()

import os

z = open("demo.txt","w")
z.write("Woops! I have deleted the content.")
z.close()

z = open("demo.txt","r")
print(z.read())

z = open("demo.txt","a")
z.write("Now, this gonna be big. Like an elephant's shadow in the room")
z = open("demo.txt","r")
print(z.read())

# new = open("new.txt","x")
# new.write("This is gonna get deleted soon.")
os.remove("new.txt")

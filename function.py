def myfunction1():
    print("Hello world")

myfunction1()

x = lambda a: a+200
print(x(20))

x = lambda a,b: a*b
print(x(34,3234))

def function2(n):
    return lambda a: a * n
mydoubler = function2(2)
print(mydoubler(123))
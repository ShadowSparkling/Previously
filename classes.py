class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunc(self):
        print("Hello my name is "+self.name)

p1 = Person("John",45)
p1.myfunc()

class Person1:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person1):
    pass

x = Student("Mike","Erik")
x.printname()

class Person2:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)

class Student1(Person2):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome, ", self.firstname, self.lastname, "to the class of ", self.graduationyear)

x1 = Student1("Mike","Olsen", 2021)
x1.welcome()
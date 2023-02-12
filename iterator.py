# str = "banana"
# myit = iter(str)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <=20:
            x=self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass1 = MyNumbers()
myiter = iter(myclass1)
for x in myiter:
    print(x)
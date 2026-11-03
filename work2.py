class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print("Hello, my name is", self.name)
        print("I am", self.age, "years old")

p1 = Person("Pond", 18)
p1.greeting()

#Task1
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


person1 =Person("Arun",26)
person1.introduce()


##Task2
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display(self):
        print(f"Title: {self.title}, Author: {self.author}")

book1 = Book("The Twited Love", "Anna huang")

book1.display()
book1.title = "Happiest Man on Earth"

book1.display()
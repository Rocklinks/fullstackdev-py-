#Day3
a =3
print(a)

b=4
pi=3.14
st = "Hello Python"
bool = True
print(f"The type of b is {type(b)}, the type of pi is {type(pi)}, th type of st is {type(st)} and the type of bool is {type(bool)}")

l =[5,8,3,7,9]
print(f"The first element is {l[0]} and the last element is {l[4]}")

dict = {"Name": "Rama", "Class":"11th","Grade":"A"}
print(dict["Grade"])

str ="123476765"
str_toint =int(str)
print(str_toint)

#Day4
list1 = [5,8,4,9]
list1.append(3)

print(list1)
list1.remove(8)
print(list1)

l = ["Answer",45.6,0,["Caldwell"]]
print(l[0])
print(l[3])

sl=["Caldwell"]
if sl in l:
    print(f"The {sl} is substring of {l}")

#Day5
tup1 = (1,5,845 ,45)
tup2 = (4,6,3,8,4)
tup3 = tup1 + tup2
print(tup3)

set1 = {23,56,7,5,6}
set2 = {5,7,32,65,8}
s3=set1.intersection(set2)
print(s3)
print(set1.union(set2))

#Day 6
dict = {"Name": "Rama", "Class":"11th","Grade":"A"}
for key,values in dict.items():
    print(f"{key}:{values}")
dict["Name"]="Rajesh"
for key,values in dict.items():
    print(f"{key}:{values}")

#Day7
a=input("Enter your name: ")
print(f"Welcome {a}")

#Day8
x,y=input("Enter x and y values: ").split()
x=int(x)
y=int(y)
print(x+y)

l = [1,2,3,4,5]
for i in l:
    if i==5:
        print(l.index(i))

#Day9
num = int(input("Enter any number: "))
if num <0:
    print(f"{num} is a negative number")
elif num==0:
    print(f"{num} is zero")
elif num>0:
    print(f"{num} is a positive number")
sum = 0
for i in range(1,11):
    sum+=i
print(sum)


for i in range(1,6):
    if i==3:
        continue
    print(i)

#Day10
def sum():
    x,y =input("Enter x,y values: ").split()
    x=int(x)
    y=int(y)
    return f"the sum of x and y is {x+y} "

print(sum())

def hello():
    return "Hello, World"

print(hello())

#Day 11
from math import sqrt
print(f"{sqrt(3):.2f}")

def square(n):
    return n*n


#Day 12
with open('1.txt','w') as file:
    file.write("Hello, Python")

with open('1.txt',"r") as file:
    content=file.read()

print(content)

#Day13
numerator = int(input("Enter any numerator: "))
denominator = int(input("Enter any denominator: "))

try:
    division = numerator /denominator
    print(division)
except ZeroDivisionError as e:
    print(f"Error: {e}")

#Day14
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age= age
        print(f"The name is {self.name} and the age is {self.age}")
p1= Person("Rocklin", 27)


#Day15
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model 
class Car(Vehicle):
    def __init__(self,brand,model,fuel_type):
        super().__init__(brand,model)
        self.fuel_type = fuel_type

car1=Car("Ambassador","maruthi","Diesel")
print(car1.brand,car1.model,car1.fuel_type)

#Day 16
import json
student = {
    "Name": "Raja Ganesh",
    "Age": 21,
    "Phone":7564423771
}

data =json.dumps(student)
print(data)

#Day 17
def fact(n):
    if n==0 or n==1:
       return 1
    return n * fact(n-1)
print(fact(2))

Day18
add = lambda x,y:x+y
print(add(5,7))

lst =[i for i in range(1,11)]
print(lst)


#Day19
def execution_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function Executed")
        return func(*args, **kwargs)
    return wrapper

@execution_decorator
def my_function():
    print("Inside my_function")

my_function()

#Day 20
import re
pattern =r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

with open('1.txt','r') as file:
    content = file.read()
emails =re.findall(pattern,content,re.MULTILINE)
print(emails)









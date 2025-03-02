#Q1
list = [1,4,5,8,5,9,1,2,3]
a=[]
for i in list:
    if i not in a:
        a.append(i)
print(a)

#Q2
mlist = [4,5,7,6,8,3]

for i in range(len(mlist)-1):
    for j in range(i+1):
        if i>j:
            continue
print(mlist[i])

#Q3
string ="welcome to aiepoch technologies python fullstack development course"
ch = "co"
            #method1
count =0
for char in string:
    if char == ch:
        count+=1
print(count)

            #method2
count =string.count(ch)
print(count)

#Q4
words = ["one..two.three", ".four.five.", "six.."]
separator = "."
c=[]
for word in words:
    a=word.split(separator)
    for i in a:
        if i!="":
            c.append(i)
print(c)

#Q5
sentence = input("Enter Sentences: ")
words = sentence.lower().split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

for word,count in word_count.items():
    print(f"{word}:{count}")


#Q6
words = input("Enter some words: ").lower().split()
a=[]
for word in words:
    if len(word)>5:
        a.append(word)
print(a)

#Q7
n =int(input("Enter a number; "))
for i in range(1,11):
    a=n*i
    print(f"{n}x{i} = {a}")


#Q8
sentence =input("Enter Sentences: ").lower()
count = 0
word = False
for char in sentence:
    if char.isalnum():
        if not word:
            count +=1
            word=True
    else:
        word = False
print(f"Number of words in sentences:  {count}")


#D9
lst=["Orange",34,15.67,"India",True,41.232]
a=[]
for i in range(len(lst)):
    if isinstance(lst[i], (int,float)) and not isinstance(lst[i],bool):
        a.append(lst[i])
print(a)

D10
try:
    num =int(input("Enter any number: "))
    if isinstance(num,int):
        print(f"{num*num}")

except ValueError as e:
    print(f"Error: {e}")    


finally:
    print("Execution Completed")

#Q11
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display_info(self):
        print(f"{self.name} earns {self.salary} Rupees Monthly")

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name,salary)
        self.department = department

    def display_info(self):
        print(f"{self.name} from the {self.department} department earns {self.salary} Rupees Monthly")

employee1 =Employee('Raja',60000)
employee1.display_info()

manager1=Manager('Arjun',80000,'HR')
manager1.display_info()


#Q12
class Student:
    def __init__(self):
        self._grade =None

    def set_grade(self,grade):
        if isinstance(grade,(int,float)) and 0<= grade<=100:
            self._grade=grade
        
    def get_grade(self):
        return self._grade

student=Student()
student.set_grade(87.7)
print(student.get_grade())

#Q13
class MathOperations:
    def add(self,a,b,*args):
        return a+b +sum(args)

math_op =MathOperations()
print(math_op.add(4,6))
print(math_op.add(1,2,3))        
        

#Q14
from math import pi
class Shape:
    def area(self):
        print("Area calculation not defined")
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return pi * self.radius **2

rect=Rectangle(5,10)
print(rect.area())

circ=Circle(4)
print(round(circ.area(),2))


#Q15
class Vehicle:
    def __init__(self,max_speed):
        self.max_speed = max_speed
    
    def display_speed(self):
        print(f"{self.max_speed} Km/h")

class Engine:
    def __init__(self,hp):
        self.hp=hp

    def display_power(self):
        print(f"{self.hp} HP")


class Car(Vehicle,Engine):
    def __init__(self, max_speed,hp):
        Vehicle.__init__(self,max_speed)
        Engine.__init__(self,hp)


car = Car(200,300,280)
car.display_speed()
car.display_power()

#AQ1
l=[4563,9412,9432,1254]
reverse=[]
rev=0
for num in l:
    rev=rev*10+num%10
    num//=10
    reverse.append(rev)

print(reverse)

#AQ2

string=input("Enter String: ").split()
a=[]
for i in string:
    if i.isdigit():
        a.append(i)

print("".join(a))

#AQ3

n=-127
flag=1 if n<0 else 0
n=abs(n)
a=0
while n>0:
    a=a*10+n%10
    n//=10
if flag:
    a=-a
print(a)














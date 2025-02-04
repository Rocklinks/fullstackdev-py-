# imported the celcius and fahreit fromt he temperature moduel
import temperature
from temperature import celcius, fahreinheit
print(f"The temperature is {celcius(45)}")
print(f"The temperature is {fahreinheit(45)}\n")


##Builtin module functions finder
import os
import inspect

def count_module_functions(module):
    functions = []
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj):
            functions.append(name)
    return len(functions)

print(f"Number of functions in the os module: {count_module_functions(os)}\n")



## Circle and rectangle
import circle
from circle import circle_area,circle_circumference
import rectangle
from rectangle import rectangle_area, rectangle_perimeter

print(f"The Are of circle is {round(circle_area(3))}")
print(f"The circumfernce of the circle is {round(circle_circumference(4))}\n")

print(f"The are of the rectangele is {rectangle_area(4,6)}")
print(f"The perimeter of the rectangle is {rectangle_perimeter(4,7)}")

import random
from random import randint
rand =[]
for i in range(10):
     num=random.randint(1,50)
     rand.append(num)

print(f"\n Maximum of the random numbers is {max(rand)} and  Minimum of the random numbers is {min(rand)}")



#Find the Factorial Function
import math_utilities
from math_utilities import factorial
print(f"The factorial is {factorial(3)}")
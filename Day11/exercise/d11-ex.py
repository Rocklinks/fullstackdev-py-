
## Math module for the pi value
import math
print(round(math.pi,2))

##Square root 64
import math
print(math.sqrt(64))

##Random Module- One number
import random
rand = random.sample(range(1,50),1)
print(rand)

# Random value from choice
import random
option=["red","blue","green","yellow"]
rand = random.choices(option)
print(rand)


## Greetings
from greetings import say_hello
print(say_hello("Rocklin"))


## math_operations
from math_operaions import add,multiply
print(add(5,7))
print(multiply(8,9))
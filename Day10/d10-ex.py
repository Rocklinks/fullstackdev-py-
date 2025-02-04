# Function with greet user
def greet():
    name=input("Enter you name: ")
    print(f"Hello {name}")
greet()

# Area of rectangle
def calculate_area_rectangle(width,height):
    area = width*height
    print(f"Area of rectangle is {area}")
calculate_area_rectangle(10,20)


#Check odd/Even

def is_even(n):
    print(n%2==0)
is_even(8)


#Function for celsius to fahreinheit
def celsius_to_fahreinheit(c):
   fahreinheit=f"{(c*9/5)+32}\u00b0"
   print(fahreinheit)
celsius_to_fahreinheit(34)

#Factorial
def fact(n):
    if n==0 or n==1:
        return 1
    return n * fact(n-1)

print(fact(2))


#Fibonacci
def fib(n):
    if n<=0:
        return []
    fibo = [0,1]
    for i in range(2,n):
        fibo.append(fibo[-1]+fibo[-2])
    return fibo
print(fib(5))


#Check for the prime
def prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
print(prime(5))

#Max of 3 num
def find_max(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num3 and num2>num1:
        return num2
    elif num3>num1 and num3>num2:
        return num3
    
print(find_max(5,10,15))



# Function to reverse the string
def reverse_string(string):
    
    return string[::-1]
string=input("Enter any strings: ")
print(reverse_string(string))



# Palindrome check
def is_palindrome(pal):
    if pal==pal[::-1]:
        return True
    else:
        return False
pal = input("Enter an strings to check for palindrome: ")
print(is_palindrome(pal))


#Generate the randome password
import random
import string
def generate_password(length):
    if length <1:
        print(f"Password must be atlest 1 ")
    characters = string.ascii_letters + string.digits
    rand = random.choices(characters, k=length)
    password = "".join(rand)
    print(password)
generate_password(5)


#File operations

#r- Read the File
#w - Write to the file
#a - append to the file
#/n for writing it in a new line

def read_file(filename):
    with open(filename,"r") as file:
        return file.read()
def write_to_file(filename,content):
    with open(filename,'a') as file:
        file.write('\n'+content)

write_to_file('1.txt',"Welcome to Python world ")
print(read_file('1.txt'))





















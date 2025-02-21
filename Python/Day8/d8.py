# Arithmatic operators
a,b=(input("Enter 2 numebers: ")).split()
a=int(a)
b=int(b)
addition = a+b
print(addition)
subtraction = a-b
print(subtraction)
mutiply = a * b
print(mutiply)
division = a / b
print(division)
floor = a // b
print(floor)
modulo = a % b
print(modulo)
exponential = a ** b
print(exponential)

# Comparison
num1,num2=(input("Enter 2 numebers: ")).split()
num1=int(num1)
num2=int(num2)
# Equals
print(f"{num1} and the {num2} are equal? {num1 == num2}")
print(f"{num1} and the {num2} are not equal? {num1 != num2}")

#greater/less
print(f"{num1} is greater than {num2}? {num1 > num2}")
print(f"{num1} is less than {num2}? {num1 < num2}")

#Greater or equal
print(f"{num1} is less than or equal to {num2}? {num1 <= num2}")
print(f"{num1} is greater than or equal to {num2}? {num1 >= num2}")


## Find Positive and Even
a = int(input("Enter any number: "))

## Odd or Even
print(f"{a} is Even" if a%2==0 else f"{a} is Odd")

if a>0 and a%2==0:
    print(f"The number {a} is Positive and Even")
elif a==0:
    print(f"The number {a} is equal to zero")
elif a>0 and a%2!=0:
    print(f"The number {a} is Positive and Odd")
else:
    print(f"The number {a} is not Positive")

#Bitwise operator
num1,num2 = input("Enter two numbers: ").split()
num1 = int(num1)
num2 = int(num2)

print(f"{num1 & num2}")
print(f"{num1 | num2}")
print(f"{num1 ^ num2}")
print(f"{~num1}")
print(f"{num1 << 2}")
print(f"{num1 >> 2}")


# Assignment Operators
number = 4
number+=5
print(f"value of number+=5 is {number}")

number = 5
number-=3
print(f"value of number-=3 is {number}")

number = 8
number*=3
print(f"value of number*=3 is {number}")

number = 9
number/=4
print(f"value of number/=4 is {number}")

number = 5
number//=2
print(f"value of number//=2 is {number}")

number = 3
number%=2
print(f"value of number%=2 is {number}")

number = 9
number**=2
print(f"value of number**=2 is {number}")


# membership Operator
fruits = ["apple", "orange","papaya","jack fruit", "mango"]
userin = input("Enter any fruit name: ").lower()

if userin in fruits:
    print(f"The fruit {userin} exists")

else:
    print(f"The fruit {userin} doesn't exits")


##Identity opeator
list1 = [3,4,5,6,7,8]
list2 = list1

## Chek if list1 is same as list 2
print(f"{list1 is list2}")
print(f"{list1 == list2}")

## check the same object in memory
print(id(list1)==id(list2))

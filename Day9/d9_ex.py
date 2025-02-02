# Conditional Statements
a = 4
print(f"{a} is Even" if a%2==0 else f"{a} is Odd")



#Vote Eligibility
age = 18

if age >= 18:
    print(" You are eligible to Caste your vote")
else:
    print(" You are not eligible to Caste your vote")




# Find which number is greater
a = 6
b = 18
c = 3
# Method 1 using if else
if a>b and a>c:
    print(f"{a} is greater")
elif b>c and b>a:
    print(f"{b} is greater")
else:
    print(f"{c} is greater")



#Method 2 using nested if else
if a>b:
    if a>c:
        print(f"{a} is greater")
    else:
        print(f"{c} is greater")
elif b>c:
    if b>a:
        print(f"{b} is greater")
else:
    print(f"{c} is greater")



#Leap year using if elif
year = 2024
if year%4==0 and year%100!=0 or year%400==0:
    print(f"The year {year} is Leap Year")
else:
    print(f"The year {year} is not a Leap Year")



# Marks with Grade
marks = 76
if marks >= 90 and marks<=100:
    print(" The Grade is A")
elif marks >=80 and marks < 90:
    print(" The Grade is B")
elif marks >=70 and marks < 80:
    print(" The Grade is B")
elif marks >=60 and marks < 70:
    print(" The Grade is C")
elif marks >=50 and marks < 60:
    print(" The Grade is D")
elif marks >=40 and marks < 50:
    print("The Grade is E")
else:
    print("Reappearance")



# Leap year using the ternary operator
year = 2032
print(f"{year} is a Leap year" if year % 4==0 and year % 100!=0 or year % 400==0 else f"{year} is not a leap year")



#Menu driven calculator app

print(" Simple Calculator program")
print("/n Enter operation")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Floor Division (//)")
print("6. Modulus (%)")
print("7. Exit")

a = float(input("Enter first number: "))
b= float(input("Enter the Second number: "))

while True:
    choose =int(input(f"Enter any number(1-7): "))
    if choose == 1:
        print(f"{a+b}")
    elif choose == 2:
        print(f"{a-b}")
    elif choose == 3:
        print(f"{a*b}")
    elif choose == 4 and b !=0:
        print(f"{a/b}")
    elif choose ==5 and b !=0:
        print(f"{a//b}")
    elif choose == 6 and b !=0:
        print(f"{a%b}")
    elif choose == 7:
        exit()
    elif choose <0 or choose>7:
        print("Enter valid number from(1-7)")
        continue



# Program to print 1- 10 using for loop
for i in range(11):
    if i==0:
        continue
    print(i)




#Factorial of a number
a=5
fact = 1
for i in range(1,a+1):
    fact= fact * i
print(f"The factorial is {fact}")



#First 10 Even number-While loop
count =0 
start = 2
while count <10:
    print(start)
    start+=2
    count+=1


 # List sum of all number   
list = [1,3,4,5,6,7]
sum=0
for i in list:
    sum+=i
print(sum)



# Sum of even numbers

list = [1,3,4,6,7,8,5,7]
sum =0
for i in range(len(list)-1):
    if list[i]%2!=0:
       continue
    #if i %2==0:
    sum+=list[i]
print(sum)


#Find given number in a list-break

a = [1,2,3,6,7,4,9]
find_num = 3
for i in range(len(a)-1):
    if a[i]==find_num:
        break
print(f"The Number {find_num} is found at index {i}")




# print numbers from 1- 10
for i in range(1,11):
    if i==5:
        print("Found")
    else:
        print(i)



## week day program
week = int(input("Enter any month number(1-7): "))

match week:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    


# Conditional Statement
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

num = 26
# if num >= 10 and num <= 20:
if 20 <= num >= 10:
    print("True")
else:
    print("False")

# Rock Paper Scissor Game with bot

import random
life = 3
score = 0
draw = 0
while life > 0:
    choices = ["rock","paper","scissor"]
    rand = random.choice(choices)
    userin = input("Type rock/Paper/Scissor: ").lower()
    if userin not in choices:
        print("Invalid keywords. Please type the rocklin/paper/scissor")
        continue
    if userin == rand :
        score+=1
        print(f"You choose {userin} and the bot choose {rand}.")
    elif userin == "paper" and rand == "scissor" or userin == "rock" and rand == "paper" or userin == "scissor" and rand == "rock":
        print(f"You choose {userin} and the bot choose {rand}.")
    elif userin == "scissor" and rand == "scissor" or userin == "rock" and rand == "rock" or userin == "paper" and rand == "paper":
        draw =1
        print(f"You choose {userin} and the bot choose {rand}. Draw So Re-enter the value ")
        continue
    #elif userin not in choices:
        #print("Invalid Choice")
    life -=1
    print(f"Your Score is {score}. Your Remaining Chances {life}")
    if score >1 and score >1:
        print("You are the winner")
print("Game over")


#Loop multiples of 15
num = 5
t = 15
list = []
for i in range(1,t+1):
    list.append(num*i)
print(list)



# Loops Odd Numbers between 50
odd_list = set()
for i in range(50):
    if i % 2 !=0:
        odd_list.add(i)
print(odd_list)


#Fibonacci Series
n =5
count =0
a,b =0,1
if n<=0:
    print("Enter positive numbers")
else:
    while count <n:
        print(a, end=" ")
        temp =a+b
        a=b
        b=temp
        count+=1


# Count sum of numbers in list excluding negaative numbers
list = [1,2,3,4,5,-6]
sum = 0
for i in list:
    if i>0: 
        sum+=i
print(sum)

# Index of string
string = "The book midnight library by haigh"
s ="e"
if s in string:
    print(string.index(s))

# Find Odd Even
a = 4
print(f"{a} is Even" if a%2==0 else f"{a} is Odd") 



month = int(input("Enter any month number(1-12): "))

match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")





















# Function to convert temperature
def temperature():
    temp=float(input("Enter the Temperature: "))
    unit=input("Enter the Unit eg:C/F/K: ").upper()
    print(f"The Temperature is {temp}\u00b0{unit}")

    unit_convert = input("Enter the unit to which you wanna convert either C/F/K: ").upper()
    
    if unit_convert=="F" and unit=="C": 
        a=f"{(temp*9/5)+32}\u00b0{unit_convert}"

        #print(f"{(temp*9/5)+32}")
    elif unit_convert=="K" and unit=="C":
        a=f"{temp+273.15}\u00b0{unit_convert}"
        #print(f"{temp+273.15}")
    elif unit_convert=="C" and unit=="F":
        a=f"{(temp-32)*5/9}\u00b0{unit_convert}"
        #print(f"{(temp-32)*5/9}")
    elif unit_convert=="K" and unit=="F":
        a=f"{(temp+459.67)*5/9}\u00b0{unit_convert}"
        #print(f"{(temp+459.67)*5/9}")    
    elif unit_convert=="C" and unit=="K":
        a=f"{temp-273.15}\u00b0{unit_convert}"
        #print(f"{temp-273.15}")
    elif unit_convert=="F" and unit=="K":
        a=f"{(temp*9/5)-459.67}\u00b0{unit_convert}"
        #print(f"{(temp*9/5)-459.67}")
    elif unit_convert=="C" and unit=="C" or unit_convert=="K" and unit=="K" or unit_convert=="F" and unit=="F":
        a=f"Can't convert {unit} to {unit_convert}"
            
    return a
    
a = temperature()
print(a)



# Function to convert the temperature to other 2 units, return as tuple
def temperatures():    
    t=float(input("Enter the Temperature: "))
    u=input("Enter the Unit eg:C/F/K: ").upper()

    if u=="C":
        a=f"{(t*9/5)+32}\u00b0F"
        b=f"{t+273.15}\u00b0K"
    elif u=="F":
        a=f"{round((t-32)*5/9)}\u00b0C"
        b=f"{round((t+459.67)*5/9)}\u00b0K"

    elif u=="K":
        a=f"{round(t-273.15)}\u00b0F"
        b=f"{(t*9/5)-459.67}\u00b0C"
 
    return a,b

print(temperatures())



#Function to calculate the grade
def calculate_grade(scores):
    average = sum(scores)/len(scores)

    if average >= 90:
        return "A"
    elif average >=80:
        return "B"
    elif average >=70:
        return "C"
    elif average >=60:
        return "D"
    else:
        return "F"

scores = [80,90,70,60,50]
print(calculate_grade(scores))



#prime number Find
def prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def find_primes(start,end):
    primes =[]
    for num in range(start,end+1): #Traditional
        if prime(num):
            primes.append(num)
    return primes

#    primes =[num for num in range(start,end+1)if prime(num)] # New method
#    return primes

start=int(input("Entert the start number: "))
end=int(input("Enter the end value: "))

print(f"Prime numbers in range are {find_primes(start,end)}")



#Count Characters as string input
def count_character(string):
    
    char_count= {}
    for char in string:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char]=1
    return char_count
string=input("Enter any set of characters: ")
print(count_character(string))



def fibonacci(num):
    if num<=0:
        return []
    fibo=[0,1]
    for i in range(2,num):
        fibo.append(fibo[-1]+fibo[-2])
    return fibo
print(fibonacci(10))



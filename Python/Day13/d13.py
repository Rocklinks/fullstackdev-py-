#Task1
try:
    num=int(input("Enter a number: "))
    print(num*num)

except ValueError as e:
    print("Error invalid Value")

except TypeError as e:
    print("Error:Invalid Type")

#Task2
try:
    num=int(input("Enter any num: "))
    print(f"Number {num} is Even" if num %2==0 else f"number {num} is Odd")
except ValueError:
    print("Error: Invalid input! Please enter a valid number")

#Task3
try:
    string=input("Enter a string: ")
    if string.isdigit():
        raise ValueError("Enter only characters ")
    elif len(string)==0:
        raise ValueError("Input cannot be empty")
        
    print(string[::-1])
except ValueError as e:
    print(f"Error: {e}")
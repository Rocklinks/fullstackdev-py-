##OOPS
"""
Object-Oriented Programming (OOP) is a programming paradigm that organizes
software design around objects rather than functions and logic. Objects represent real-
world entities, encapsulating data (attributes) and behavior (methods) into a single
unit
"""

## Task2
class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def __str__(self):
        return f"Employee[ID: {self.emp_id}, Name: {self.name}, Department: {self.department}, Salary: {self.salary}]"

em1 = Employee(101, "Alice", "HR", 50000)
em2 = Employee(102, "Bob", "Projects", 70000)

print(em1)
print(em2)

"""
#Benefits of the OOP Approach

Encapsulation: The Employee class groups all relevant data and behavior, improving data integrity and modularity.

Code Reusability: Creating multiple employee objects is easier compared to managing separate variables.

Scalability: We can extend the Employee class with new attributes and methods (e.g., calculate_bonus(), update_salary()).

Better Readability & Maintainability: The class-based structure makes it easier to understand and maintain.

Abstraction: Users of the Employee class do not need to know its internal implementation, just how to interact with it.
"""

"""
The __str__() method provides a meaningful string representation when printing an Employee object, making debugging and logging easier.

Let me know if you need any modifications! 
"""


#Task3
class Employee:
    company_name = "TechCorp"  # Class Variable

    def __init__(self, name, age):
        self.name = name  # Instance Variable
        self.age = age    # Instance Variable
    
    @staticmethod
    def company_policy():
        return "Follow ethical practices"  # Static Variable

# Creating Instances
emp1 = Employee("Alice", 25)
emp2 = Employee("Bob", 30)

print(emp1.name)  
print(emp2.company_name)  
print(Employee.company_policy())  


class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient funds or invalid amount")

    def check_balance(self):
        return f"Current Balance: {self.__balance}"

# Testing the BankAccount class
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print(account.check_balance())


class School:
    school_name = "Greenwood High"  # Class Variable

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name  # Modifies class variable

    @staticmethod
    def school_motto():
        return "Education for All"  

# Using class method
School.change_school("Blue Ridge Academy")
print(School.school_name)

# Using static method
print(School.school_motto())  



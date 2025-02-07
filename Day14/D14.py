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

# Creating employee objects
emp1 = Employee(101, "Alice", "HR", 50000)
emp2 = Employee(102, "Bob", "IT", 70000)

# Printing employee details
print(emp1)
print(emp2)
class Vehicle:
    def fuel_type(self):
        pass

class PetrolCar(Vehicle):
    def fuel_type(self):
        return "Petrol"

class ElectricCar(Vehicle):
    def fuel_type(self):
        return "Electric"

# Example Usage
petrol_car = PetrolCar()
electric_car = ElectricCar()
print(petrol_car.fuel_type())  # Output: Petrol
print(electric_car.fuel_type())  # Output: Electric

class LightSystem:
    def turn_on_lights(self):
        return "Lights turned on"

class SecuritySystem:
    def activate_alarm(self):
        return "Alarm activated"

class SmartHome(LightSystem, SecuritySystem):
    def home_status(self):
        return "Smart home is operational"

# Example Usage
smart_home = SmartHome()
print(smart_home.turn_on_lights())  # Output: Lights turned on
print(smart_home.activate_alarm())  # Output: Alarm activated
print(smart_home.home_status())  # Output: Smart home is operational

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

class Manager(Employee):
    def __init__(self, name, age, employee_id, department, team_size):
        super().__init__(name, age, employee_id, department)
        self.team_size = team_size

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.employee_id}, Department: {self.department}, Team Size: {self.team_size}"

# Example Usage
manager = Manager("Alice", 35, "M123", "IT", 10)
print(manager.display_info())
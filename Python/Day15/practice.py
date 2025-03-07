# #1
# class Payment:
#     def process_payment(self):
#         pass  
# class Credit_card(Payment):
#     def process_payment(self):
#         return "Processing payment via Credit Card"
        
# class Paypal(Payment):
#     def process_payment(self):
#         return "Processing payment via Paypal"
        
# method = Paypal()
# print(method.process_payment())

# method2= Credit_card()
# print(method2.process_payment())

# #2
# class car:
#     def start_engine(self):
#         return "Engine Started"

# class MusicSystem:
#     def play_music(self):
#         return "Music playing"
        
# class SmartCar(car,MusicSystem):
#     def car_status(self):
#         return "Smart Car is Ready"
# car = SmartCar()
# print(car.start_engine())
# print(car.play_music())
# print(car.car_status())

# #3
# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
# class Car(Vehicle):
#     def __init__(self, make, model, num_doors):
#         super().__init__(make,model)
#         self.num_doors = num_doors
    
# class Electric(Car):
#     def __init__(self, make, model, num_doors, battery_capacity):
#         super().__init__(make,model,num_doors)
#         self.battery_capacity = battery_capacity

# car1 = Electric("Ford","Figo 2019",4,"6000Ah")
# print(f"Make is {car1.make}")
# print(f"Model is {car1.model}")
# print(f"Number of doors {car1.num_doors}")
# print(f"Battery Capacity is {car1.battery_capacity}")

# private method
# class bankaccount:
#     def __init__(self,balance=0):
#         self.__balance = balance

#     def get_balance(self):
#         return self.__balance
    
#     def withdraw(self,amount):
#         self.amount = amount
#         if self.amount>0 and self.__balance > amount:
#             self.__balance -= amount
#             return f"Successfully withdrawn the amount {self.amount}"
#         else:
#             return f"Failed to withdraw {self.amount}"

#     def deposit(self,amount):
#         self.amount =amount
#         if amount >0:
#             self.__balance+=amount
#             return f"The deposit amount is {self.__balance}"


# person = bankaccount()
# print(person.deposit(50000))
# print(person.withdraw(5000))
# print(f"The current balance is {person.get_balance()}")

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     return "Drive!"

# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     return "Sail!"

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     return "Fly!"

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object

# print(f"Model is {car1.model}, brand is {car1.brand}. {car1.move()} safely")
# print(f"Model is {boat1.model}, brand is {boat1.brand}. {boat1.move()} safely")
# print(f"Model is {plane1.model}, brand is {plane1.brand}. {plane1.move()} safely")




# #Inheritance class polymorphism
# class Vehicles:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         pass

# class Car(Vehicles):
#     def move(self):
#         return "Drive"

# class Boat(Vehicles):
#   def move(self):
#     return "Sail!"

# class Plane(Vehicles):

#   def move(self):
#     return "Fly!"

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object

# print(f"Model is {car1.model}, brand is {car1.brand}. {car1.move()} safely")
# print(f"Model is {boat1.model}, brand is {boat1.brand}. {boat1.move()} safely")
# print(f"Model is {plane1.model}, brand is {plane1.brand}. {plane1.move()} safely")

# class Parent: 
#   def show(self): 
#     return "Parent" 
# class Child(Parent): 
#   def show(self): 
#     return "Child" 
# obj = Child() 
# print(obj.show())   





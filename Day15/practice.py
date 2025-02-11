#1
class Payment:
    def process_payment(self):
        pass  
class Credit_card(Payment):
    def process_payment(self):
        return "Processing payment via Credit Card"
        
class Paypal(Payment):
    def process_payment(self):
        return "Processing payment via Paypal"
        
method = Paypal()
print(method.process_payment())

method2= Credit_card()
print(method2.process_payment())

#2
class car:
    def start_engine(self):
        return "Engine Started"

class MusicSystem:
    def play_music(self):
        return "Music playing"
        
class SmartCar(car,MusicSystem):
    def car_status(self):
        return "Smart Car is Ready"
car = SmartCar()
print(car.start_engine())
print(car.play_music())
print(car.car_status())

#3
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make,model)
        self.num_doors = num_doors
    
class Electric(Car):
    def __init__(self, make, model, num_doors, battery_capacity):
        super().__init__(make,model,num_doors)
        self.battery_capacity = battery_capacity

car1 = Electric("Ford","Figo 2019",4,"6000Ah")
print(f"Make is {car1.make}")
print(f"Model is {car1.model}")
print(f"Number of doors {car1.num_doors}")
print(f"Battery Capacity is {car1.battery_capacity}")


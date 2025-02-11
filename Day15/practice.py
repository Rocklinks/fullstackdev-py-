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



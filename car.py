class Car (object):
    def __init__(self, model, color, company,speed_limit):
        self.color = color
        self.model = model
        self.company = company
        self.speed_limit = speed_limit
        
    def start(self):
        print("Starting")
    
    def stop(self):
        print("Stoping")
    
    def acclerate(self):
        print("Accelerating")

    def decelerate(self):
        print("Braking")

    def change_gear(self, gear_type):
        print("Change Gear")

Audi = Car("R8", "Yellow" , "Audi", 330) 
print(Audi.start()),
print(Audi.stop())
print(Audi.acclerate())
print(Audi.decelerate())
print(Audi.change_gear(1))


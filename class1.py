class Auto:
    def __init__(self):
        self.number = []
        self.power = 0
    def get_tax(self,min_rate=12,max_rate=25):
        rate = max_rate if self.power >100 else min_rate
        return rate * self.power    

class Bus(Auto):
    def get_tax(self,min_rate=15,max_rate=15):
        return super().get_tax(min_rate,max_rate)

class InterCityBus(Bus):

    def __init__(self):
        self.city = ""
        super().__init__()

    def get_city(self):
        return self.city    


auto = Auto()
auto.power = 101
print(auto.get_tax())

bus = Bus()
bus.power = 300
print(bus.get_tax())

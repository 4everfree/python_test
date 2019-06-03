class Auto:
    
    count = 0
    objects = []

    def __init__(self):
        self.number = ""
        self.power = 0

        Auto.count += 1 
        Auto.objects.append(self) 

    @staticmethod
    def set_powers(power):
        for obj in Auto.objects:
            obj.power = power


class Bus(Auto):
    pass


auto1 = Auto()
auto2 = Auto()
bus = Bus()

print(Auto.count)

print(auto1.count)

auto1.count = 10

print(Auto.count)

print(auto1.count)

Auto.set_powers(300)

for obj in Auto.objects:
    print(obj.power)

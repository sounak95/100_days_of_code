
class Car:
    wheels =4
    def __init__(self, model):
        self.model = model



c1=Car("bmw")
c2 = Car("audi")

Car.wheels = 5
print(c1.wheels, c1.model)
print(c2.wheels, c2.model)

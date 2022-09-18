

class Student:
    def __init__(self, name, roll, model, ram):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop(model, ram)

    def show(self):
        print(self.name, self.roll)
        self.lap.show()

    class Laptop():
        def __init__(self, model, ram):
            self.model = model
            self.ram= ram

        def show(self):
            print(self.model, self.ram)

s1= Student("sounak", "72", "def", "32gb")
s1.show()
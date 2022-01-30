class Vehicle:

    # colour = "White"

    def __init__(self, name, max_speed, mileage, colour="White"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.colour = colour

    def print(self):
        print(f"Colour: {self.colour}, Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}")

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers."


class Bus(Vehicle):
    # def print(self):
    #     print(f"Vehicle Name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage}")
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


class Car(Vehicle):
    pass


School = Bus("School Volvo", 180, 12)
Audi_Q5 = Car("Audi Q5", 240, 18)
School.print()
Audi_Q5.print()
print(School.seating_capacity())

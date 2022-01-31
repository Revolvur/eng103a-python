# class Vehicle:
#
#     # colour = "White"
#
#     def __init__(self, name, max_speed, mileage, colour="White", capacity):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.colour = colour
#         self.capacity = capacity
#
#     def print(self):
#         print(f"Colour: {self.colour}, Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}")
#
#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers."
#
#     def fare(self):
#         return self.capacity * 100
#
#
# class Bus(Vehicle):
#     # def print(self):
#     #     print(f"Vehicle Name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage}")
#     def seating_capacity(self, capacity=50):
#         return super().seating_capacity(capacity)
#
#     def fare(self, capacity=50):
#         return self.capacity * 100
#
# class Car(Vehicle):
#     pass
#
#
# School = Bus("School Volvo", 180, 12, "White", 50)
# Audi_Q5 = Car("Audi Q5", 240, 18, "", 4)
# School.print()
# Audi_Q5.print()
# print(School.seating_capacity())

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def fare(self):
        # return self.capacity * 100 * 1.1
        amount = super().fare()
        amount += amount * 10 / 100
        return amount


School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
print(type(School_bus))
print(isinstance(School_bus, Vehicle))

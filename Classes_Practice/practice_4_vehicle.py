class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def print(self):
        print(f"Vehicle Name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage}")


class Bus(Vehicle):
    # def print(self):
    #     print(f"Vehicle Name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage}")
    pass

School = Bus("School Volvo", 180, 12)
print(School.mileage, School.max_speed)
print(School, type(School))
School.print()

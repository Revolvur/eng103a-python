class Car:
    def __init__(self, colour, mileage):
        self.colour = colour
        self.mileage = mileage

    def print(self):
        print(f"The {self.colour} car has {self.mileage}.")


blue_car = Car("blue", "20,000")
red_car = Car("red", "30,000")
blue_car.print()
red_car.print()
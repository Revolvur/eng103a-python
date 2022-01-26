# import car_class
#
# new_car = car_class.Car(220)
# new_car.accelerate(100)
# print(new_car)
#
# print(__name__)   # "__main__ # set to main unless imported to different module

from car_class import Car, something_else

new_car = Car(220)
# new_car.accelerate(100)
# print(new_car)

print(something_else)

print(__name__)   # "__main__ # set to main unless imported to different module

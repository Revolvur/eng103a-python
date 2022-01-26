# class Car:
#     def __init__(self, current_speed, speed_increase=0, max_speed=100):
#         # dunder init method, set a max_speed attribute (and a current speed)
#         # implement the following methods:
#         self.max_speed = max_speed
#         self.current_speed = self.accelerate(speed_increase)
#
#     # accelerate
#     # brake
#
#     def accelerate(self, speed_increase):
#         # add the increase on to the current speed
#         current_speed = self.current_speed
#         max_speed = self.max_speed
#         current_speed += speed_increase
#         return self.max_speed
#
#
#
#     def brake(self):
#         pass
#
#
# my_car = Car(69)
# print(my_car.accelerate(69))


class Car:
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.__speed = 0  # stationary to start with

    def accelerate(self, speed_increase): # setters
        # self.speed += speed_increase
        # if self.speed + speed_increase > self.max_speed:
        #     self.speed = self.max_speed  # puts it down to max speed if over limit
        # else:
        #     self.speed += speed_increase

        self.__speed = min(self.max_speed, self.__speed + speed_increase)

    def brake(self, brake_brake):
        # self.speed += brake_brake
        # # return self.speed
        # if self.speed - brake_brake < 0:
        #     self.speed = 0
        # else:
        #     self.speed -= brake_brake
        self.__speed = max(0, self.__speed - brake_brake)

    def get_speed(self):
        return self.__speed

car = Car(180)
car.__speed = 30000
print(car.__speed)
print(car.get_speed())
# my_car = Car(100)
# print(car.max_speed)
# print(car.speed)
# car.accelerate(50)
# print(car.speed)
# car.accelerate(300000)
# print(car.speed)
# car.brake(50)
# print(car.brake(50))

print("Car Class __name__ is: " + __name__)

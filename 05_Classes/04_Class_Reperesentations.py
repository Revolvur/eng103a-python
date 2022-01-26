# class Location:
#     def __init__(self, latitude, longitude):
#         self.latitude = latitude
#         self.longitude = longitude
#
#     def __repr__(self): # further representation of our object
#         return f"Location(latitude={self.latitude}, longitude={self.longitude})"
#
#     def __str__(self):  # string representation
#         return f"({self.latitude}, {self.longitude})"
#
# bham_academy = Location(latitude=69.6969, longitude=-5.323)
# print(repr(bham_academy))
# print(bham_academy) # will provide string unless repr
#
# print(f"Sparta Global brum academy located at {bham_academy}.")

class Dog:
    def __init__(self, age):
        self.age = age

    def __repr__(self):  # repr used for logging and debugging
        return f"Dog(age={self.age})"

    def __str__(self):
        return f"A {self.age} year old Dog."

    def __format__(self, format_spec):  # format spec provided after colon
        if format_spec == "dog":
            return f"A {self.age * 7} dog-years old Dog"
        else:
            return self.__str__()


fido = Dog(5)
print(fido)
print(f"Fido is a {fido:dog}")

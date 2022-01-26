# OOP - Object Orientated Programming

# the 'bad' way

class Dog:  # Class names are always first letter upper case
    def __init__(self, dog_breed, hair_length, legs=4, criminal_record=None):  # Initialisation, dunder (double underscore) init,
        # legs=4 is a default variable
        self.animal_kind = "canine"  # any attributes (self....) go here
        self.legs = legs
        self.breed = dog_breed
        self.criminal_record = criminal_record
        self.hair_length = self.set_hair_length(hair_length)
        print(self.bark())

    @staticmethod  # static as there is nothing in here that doesn't mess with any attributes
    def set_hair_length(hair_length):
        if hair_length in ("short", "medium", "long"):
            return hair_length
        else:
            print("Hair length must be short, medium or long. Defaulting to medium")
            return "medium"

    def bark(self):  # method  # self = referring to the current class
        return "Woof! I am a " + self.animal_kind

    def loud_bark(self):
        return self.bark().upper()


fido = Dog("Dalmatian",
           "short")  # fido is an instance (object) of the Dog class, it has access to all of dog's variables and methods
print(fido, type(fido))
print(fido.animal_kind)
print(fido.loud_bark())

# lassie = Dog()  # Instantiation - i.e. creating an INSTANCE of a class
# pluto = Dog()
# print(fido.animal_kind)
# fido.animal_kind = "giraffe"
# print(fido.animal_kind)
# Dog.animal_kind = "arachnid"
# print(lassie.animal_kind)
# print(fido.animal_kind)  # objects cannot be easily overwritten by overriding class

fido.legs = 3
print(fido.legs)
print(fido.breed)
lassie = Dog("Collie", "yes", criminal_record="Arson")
print(lassie.breed)
print(lassie.set_hair_length)
print(lassie.legs)

# first argument for method is self

# class Chihuahua:
#     animal_kind = "best dog"
#
#     def cute(self):
#         return "Grrr.... I am the " + self.animal_kind
#
#     def loud_cute(self):
#         return self.cute().upper() + "!"
#
#
# steven = Chihuahua()
# lucy = Chihuahua()
#
# print(steven.animal_kind)
# print(steven.cute)
# print(steven.loud_cute())
# steven.animal_kind = "best and cutest dog"
# print(steven.animal_kind)
# print(lucy.animal_kind)

# OOP - Object Orientated Programming

# the 'bad' way

class Dog:  # Class names are always first letter upper case

    animal_kind = "canine"  # class variable

    def bark(self):  # method  # self = referring to the current class
        return "Woof! I am a " + self.animal_kind

    def loud_bark(self):
        return self.bark().upper()


fido = Dog()  # fido is an instance (object) of the Dog class, it has access to all of dog's variables and methods
print(fido, type(fido))
print(fido.animal_kind)
print(fido.loud_bark())

lassie = Dog()  # Instantiation - i.e. creating an INSTANCE of a class
pluto = Dog()
print(fido.animal_kind)
Dog.animal_kind = "arachnid"
print(fido.animal_kind)
# print(lassie.animal_kind)
# fido.animal_kind = "feline"
# print(fido.animal_kind)
# print(lassie.animal_kind)

# # first argument for method is self
#
# class Chihuahua:
#     animal_kind = "best dog"
#
#     def cute(self):
#         return "Grrr.... I am the " + self.animal_kind + "."
#
#
# steven = Chihuahua()
#
# print(steven.animal_kind)

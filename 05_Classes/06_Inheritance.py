# Inheritance and Polymorphism (can take many forms) - even though they're inherited but can still take different forms

class Mammal:
    def __init__(self, mammal_name):
        self.warm_blooded = True
        self.name = mammal_name

    def reproduce(self):
        print("Giving birth to live young.")


class Platypus(Mammal):
    def __init__(self, name):
        super().__init__(name)
        self.poisonous_barbs = True

    def reproduce(self):
        print("Laying eggs")


# m = Mammal()
# m.reproduce()

class Horse(Mammal):  # inherits mammal class, all methods from Mammal become available to horse
    def __init__(self, horse_name, jockey):
        super().__init__(horse_name)  # when we init horse we're also going to run init method of superclass
        self.legs = 4  # otherwise horse init will override mammal init
        self.jockey = jockey

    def pregnancy(self):
        print("Wait 11 months...")
        super().reproduce()


class Pony(Horse):
    def __init__(self, pony_name, cuteness_rating=10):
        super().__init__(pony_name, None)

    def give_birth(self):
        super().reproduce()


# p = Pony("Twinkle Toes")
# print(p.legs)
# p.pregnancy()

# m = Mammal("Charlie")
#
# h = Horse("pele", "vistoso")  # inherited warm blooded and reproduce
# print(h.warm_blooded)
# h.reproduce()
#
# #  example user and super user, super user can inherit permissions from user and other permissions as super user

perry = Platypus("Perry")
print(perry.reproduce())

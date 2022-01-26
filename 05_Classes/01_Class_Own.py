class Chihuahua:
    def __init__(self, hair_type):
        self.animal_kind = "best dog"  # Initialisation, dunder (double underscore) init
        self.aggression = 8  # out of 10  # any attributes go here
        self.hair = hair_type

    def cute(self):
        return "Grrr.... I am the " + self.animal_kind

    def loud_cute(self):
        return self.cute().upper() + "!"


harold = Chihuahua("curly")
steven = Chihuahua("short")
wendy = Chihuahua("fluffy")
steven.aggression = 3
wendy.aggression = 4

# print(steven.animal_kind)
# print(steven.loud_cute())
# steven.animal_kind = "best and cutest dog"
print(steven.animal_kind)
print(wendy.animal_kind)
print(steven.hair)
print(wendy.hair)
print(steven.aggression)
print(harold.aggression)
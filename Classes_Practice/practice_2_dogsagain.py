class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):  # initialise
        self.name = name
        self.age = age

    def description(self):  # instance method
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):  # instance method
        return f"{self.name} says {sound}"


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


class Dachshund(Dog):
    def speak(self, sound="Yap"):
        return super().speak(sound)


class Bulldog(Dog):
    def speak(self, sound="Woof"):
        return super().speak(sound)


miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
miles = JackRussellTerrier("Miles", 4)
print(miles.speak())

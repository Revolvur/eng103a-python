class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):  # instance method
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} says {sound}"


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"


class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass


miles = JackRussellTerrier("Miles", 4)
print(miles.speak())
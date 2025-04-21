# Base Class
class Superhero:
    def __init__(self, name, power_level):
        self.name = name
        self.__power_level = power_level  # encapsulated attribute

    def introduce(self):
        print(f"I am {self.name}, my power level is {self.__power_level}.")

    def use_power(self):
        print(f"{self.name} uses a generic power!")

    def get_power_level(self):
        return self.__power_level

# Inherited Class 1
class Speedster(Superhero):
    def use_power(self):
        print(f"{self.name} dashes with lightning speed! ⚡")

# Inherited Class 2
class Flyer(Superhero):
    def use_power(self):
        print(f"{self.name} soars through the skies! 🕊️")

# Test it out
hero1 = Speedster("Flashlight", 9000)
hero2 = Flyer("Skyrider", 8500)

hero1.introduce()
hero1.use_power()

hero2.introduce()
hero2.use_power()

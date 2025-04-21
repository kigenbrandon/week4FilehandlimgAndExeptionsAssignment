import time
import random

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

    def move_speed(self):
        raise NotImplementedError("Subclasses must implement this method")

    def simulate_movement(self):
        speed = self.move_speed()
        print(f"{self.__class__.__name__} starting journey...")
        for i in range(5):
            print("🚘" * (i + 1))
            time.sleep(1 / speed)  # faster speed = shorter delay
        print(f"{self.__class__.__name__} finished moving!\n")

class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

    def move_speed(self):
        return 2  # moderate speed

class Plane(Vehicle):
    def move(self):
        print("Flying through the clouds ✈️")

    def move_speed(self):
        return 5  # fastest

class Boat(Vehicle):
    def move(self):
        print("Sailing on the waves 🚤")

    def move_speed(self):
        return 1  # slowest

# Polymorphic behavior with animated movement
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
    v.simulate_movement()

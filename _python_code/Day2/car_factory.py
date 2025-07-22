class Car:
    # This is the blueprint for a Car

    def __init__(self, color, brand, num_wheels=4):
        # This is a special method called the "constructor".
        # It's like the initial assembly line for a new car.
        # 'self' refers to the specific car object being created.
        self.color = color         # Set the color attribute for this car
        self.brand = brand         # Set the brand attribute for this car
        self.num_wheels = num_wheels # Set the number of wheels (default to 4)

    def accelerate(self):
        # This is a method (behavior) for a Car object
        print(f"The {self.color} {self.brand} car is accelerating!")

    def brake(self):
        # Another method
        print(f"The {self.color} {self.brand} car is braking.")

# Creating an object (a specific car) from the Car class
my_red_car = Car("red", "Toyota")
johns_blue_car = Car("blue", "Honda")
my_red_car.accelerate()
my_red_car.brake()

# Accessing attributes
print(f"My car's color: {my_red_car.color}")
print(f"John's car's brand: {johns_blue_car.brand}")

# Setting (modifying) an attribute
my_red_car.color = "yellow"
print(f"My car's new color: {my_red_car.color}")
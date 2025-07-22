class Vehicle: # General blueprint
    def __init__(self, num_wheels, top_speed):
        self.num_wheels = num_wheels
        self.top_speed = top_speed

    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle): # Car inherits from Vehicle
    def __init__(self, color, brand):
        super().__init__(4, 200) # Call the parent (Vehicle) constructor
        self.color = color
        self.brand = brand

    def accelerate(self): # Car has its own specific method
        print(f"The {self.color} {self.brand} car is accelerating!")

class Motorcycle(Vehicle): # Motorcycle also inherits from Vehicle
    def __init__(self, engine_size):
        super().__init__(2, 180) # Call the parent (Vehicle) constructor
        self.engine_size = engine_size

    def wheelie(self):
        print(f"The motorcycle is doing a wheelie!")

my_car = Car("green", "BMW")
my_car.move() # Car can use the Vehicle's move method
my_car.accelerate()

my_motorcycle = Motorcycle("1000cc")
my_motorcycle.move()
my_motorcycle.wheelie()
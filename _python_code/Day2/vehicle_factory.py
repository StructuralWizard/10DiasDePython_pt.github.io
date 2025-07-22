class Vehicle: # Projeto geral
    def __init__(self, num_wheels, top_speed):
        self.num_wheels = num_wheels
        self.top_speed = top_speed

    def move(self):
        print("O veículo está se movendo.")

class Car(Vehicle): # Carro herda de Veículo
    def __init__(self, color, brand):
        super().__init__(4, 200) # Chama o construtor do pai (Veículo)
        self.color = color
        self.brand = brand

    def accelerate(self): # Carro tem seu próprio método específico
        print(f"O carro {self.color} {self.brand} está acelerando!")

class Motorcycle(Vehicle): # Motocicleta também herda de Veículo
    def __init__(self, engine_size):
        super().__init__(2, 180) # Chama o construtor do pai (Veículo)
        self.engine_size = engine_size

    def wheelie(self):
        print(f"A motocicleta está empinando!")

my_car = Car("verde", "BMW")
my_car.move() # Carro pode usar o método mover do Veículo
my_car.accelerate()

my_motorcycle = Motorcycle("1000cc")
my_motorcycle.move()
my_motorcycle.wheelie()
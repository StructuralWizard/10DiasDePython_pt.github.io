class Car:
    # Este é o projeto para um Carro

    def __init__(self, color, brand, num_wheels=4):
        # Este é um método especial chamado "construtor".
        # É como a linha de montagem inicial para um novo carro.
        # 'self' se refere ao objeto carro específico que está sendo criado.
        self.color = color         # Define o atributo de cor para este carro
        self.brand = brand         # Define o atributo de marca para este carro
        self.num_wheels = num_wheels # Define o número de rodas (padrão para 4)

    def accelerate(self):
        # Este é um método (comportamento) para um objeto Carro
        print(f"O carro {self.color} {self.brand} está acelerando!")

    def brake(self):
        # Outro método
        print(f"O carro {self.color} {self.brand} está freando.")

# Criando um objeto (um carro específico) a partir da classe Carro
my_red_car = Car("vermelho", "Toyota")
johns_blue_car = Car("azul", "Honda")
my_red_car.accelerate()
my_red_car.brake()

# Acessando atributos
print(f"A cor do meu carro: {my_red_car.color}")
print(f"A marca do carro do João: {johns_blue_car.brand}")

# Definindo (modificando) um atributo
my_red_car.color = "amarelo"
print(f"A nova cor do meu carro: {my_red_car.color}")

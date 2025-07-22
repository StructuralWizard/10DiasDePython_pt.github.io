import random

# Constantes
ROOMS = ["Salão", "Cozinha", "Biblioteca", "Masmorra", "Jardim"]
ITEMS = ["espada", "poção", "escudo"]
MONSTERS = ["Goblin", "Troll", "Esqueleto"]

# Variável global
found_key = False

def print_welcome():
    """Imprime a mensagem de boas-vindas com arte ASCII."""
    print("""
    🧟‍♂️ LABIRINTO DE MONSTROS 🧟‍♀️
    Escape do labirinto, derrote monstros e encontre a chave!
    """)  # Manipulação e impressão de strings

def create_player(name):
    """Retorna um novo dicionário de jogador."""
    return {
        "name": name,
        "health": 100,
        "inventory": [],
        "location": random.choice(ROOMS)  # Módulo random
    }

def describe_room(room):
    """Descreve a sala atual."""
    print(f"\nVocê está agora no(a) {room}.")
    if random.random() < 0.4:  # Declaração condicional
        item = random.choice(ITEMS)
        print(f"Você encontrou um(a) {item}!")
        return item
    return None

def encounter_monster(player):
    """Encontro aleatório com monstro com chance de luta."""
    if random.random() < 0.3:
        monster = random.choice(MONSTERS)
        print(f"\n⚔️ Um {monster} selvagem aparece!")
        if "sword" in player["inventory"]:
            print("Você o derrota com sua espada!")
        else:
            player["health"] -= 20
            print("Você não tem espada! Você se machucou!")
            print(f"Vida: {player['health']}")
            if player["health"] <= 0:
                print("💀 Você morreu. Fim de jogo.")
                exit()

def move_to_new_room(player):
    """Move o jogador para uma nova sala aleatória."""
    previous = player["location"]
    player["location"] = random.choice([r for r in ROOMS if r != previous])

def check_for_key(player):
    """Verifica se o jogador encontra a chave."""
    global found_key
    if not found_key and random.random() < 0.2:
        found_key = True
        print("🔑 Você encontrou a chave mágica!")
        player["inventory"].append("chave mágica")

def game_loop(player):
    """Loop principal do jogo usando recursão."""
    if found_key:
        print(f"\n🎉 Parabéns, {player['name']}! Você escapou do labirinto!")
        return # Termina o jogo se a chave for encontrada

    item = describe_room(player["location"])
    if item:
        player["inventory"].append(item)
    
    encounter_monster(player)
    check_for_key(player)

    # Loop while e formatação de string com f-strings
    while True:
        choice = input("\nVocê quer se mover para outra sala? (sim/não): ").lower()
        if choice in ["sim", "s"]:
            move_to_new_room(player)
            game_loop(player)  # Recursão
            break
        elif choice in ["não", "n", "nao"]:
            print("🛌 Você escolheu descansar. Fim de jogo.")
            break
        else:
            print("Por favor, responda sim ou não.")

# Programa principal
def main():
    """Inicia o jogo."""
    print_welcome()
    name = input("Digite seu nome, aventureiro: ")
    player = create_player(name)  # Função com entradas/saídas
    game_loop(player)

if __name__ == "__main__":
    main()

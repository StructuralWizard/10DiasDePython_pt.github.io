import random

# Constants
ROOMS = ["Hall", "Kitchen", "Library", "Dungeon", "Garden"]
ITEMS = ["sword", "potion", "shield"]
MONSTERS = ["Goblin", "Troll", "Skeleton"]

# Global variable
found_key = False

def print_welcome():
    """Prints the welcome message with ASCII art."""
    print("""
    🧟‍♂️ MONSTER MAZE 🧟‍♀️
    Escape the maze, defeat monsters, and find the key!
    """)  # String manipulation and printing

def create_player(name):
    """Returns a new player dictionary."""
    return {
        "name": name,
        "health": 100,
        "inventory": [],
        "location": random.choice(ROOMS)  # Random module
    }

def describe_room(room):
    """Describes the current room."""
    print(f"\nYou are now in the {room}.")
    if random.random() < 0.4:  # Conditional statement
        item = random.choice(ITEMS)
        print(f"You found a {item}!")
        return item
    return None

def encounter_monster(player):
    """Random monster encounter with chance of fight."""
    if random.random() < 0.3:
        monster = random.choice(MONSTERS)
        print(f"\n⚔️ A wild {monster} appears!")
        if "sword" in player["inventory"]:
            print("You defeat it with your sword!")
        else:
            player["health"] -= 20
            print("You have no sword! You got hurt!")
            print(f"Health: {player['health']}")
            if player["health"] <= 0:
                print("💀 You have died. Game Over.")
                exit()

def move_to_new_room(player):
    """Moves the player to a new random room."""
    previous = player["location"]
    player["location"] = random.choice([r for r in ROOMS if r != previous])

def check_for_key(player):
    """Checks if the player finds the key."""
    global found_key
    if not found_key and random.random() < 0.2:
        found_key = True
        print("🔑 You found the magic key!")
        player["inventory"].append("magic key")

def game_loop(player):
    """Main game loop using recursion."""
    if found_key:
        print(f"\n🎉 Congratulations, {player['name']}! You escaped the maze!")
        return # End the game if key is found

    item = describe_room(player["location"])
    if item:
        player["inventory"].append(item)
    
    encounter_monster(player)
    check_for_key(player)

    # While loop & string formatting with f-strings
    while True:
        choice = input("\nDo you want to move to another room? (yes/no): ").lower()
        if choice in ["yes", "y"]:
            move_to_new_room(player)
            game_loop(player)  # Recursion
            break
        elif choice in ["no", "n"]:
            print("🛌 You chose to rest. Game Over.")
            break
        else:
            print("Please answer yes or no.")

# Main program
def main():
    """Starts the game."""
    print_welcome()
    name = input("Enter your name, adventurer: ")
    player = create_player(name)  # Function with inputs/outputs
    game_loop(player)

if __name__ == "__main__":
    main()

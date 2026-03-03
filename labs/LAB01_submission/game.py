"""
Lab 1: Text-Based Adventure RPG
================================
Lewis Campbell

MYSTIC MOUNTAIN - Fight your way from the mountain to the beach!

Run with: python game.py
"""

import random


# =============================================================================
# Dice Utilities
# =============================================================================

def roll_d20():
    """Roll a 20-sided die."""
    return random.randint(1, 20)


def roll_dice(num_dice, sides):
    """Roll multiple dice and return the total. E.g., roll_dice(2, 6) for 2d6."""
    return sum(random.randint(1, sides) for _ in range(num_dice))


# =============================================================================
# Item Classes
# =============================================================================

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, player, location=None):
        pass

    def __str__(self):
        return f"{self.name}: {self.description}"


class MudPie(Item):
    def __init__(self):
        super().__init__("Mud Pie", "Increases Health 25+")

    def use(self, player, location=None):
        player.health = min(player.health + 25, player.max_health)
        print(f"There's a lesson in here about taking L's...\n")
        print(f"Health: {player.health}/{player.max_health}")


class BusinessShield(Item):
    def __init__(self):
        super().__init__("Business Shield", "Forged in the basement next to the screen printing equipment")

    def use(self, player, location=None):
        player.defense = player.defense + 3
        player.strength = player.strength + 5
        print(f"You equip the shield of Business Expierience! Defense: {player.defense}")
        print(f" At least {player.defense} is enough to see the sword coming, before it hits you in the face!")


class MarketingMace(Item):
    def __init__(self):
        super().__init__("Marketing Mace", "Now you have their attention, what are you going to do with it?")

    def use(self, player, location=None):
        player.strength = player.strength + 5


class HolyHandGrenade(Item):
    def __init__(self):
        super().__init__("Holy Hand Grenade", " Tis` but a Scratch ")

    def use(self, player, location=None):
        if location and location.enemies:
            print(" Okay but other than the Holy Hand Grenade, what have the Romans ever done for us?")
            for enemy in location.enemies:
                print(f"{enemy.name} is dead. Anyway...")
            location.enemies.clear()
        else:
            print("You really had a Holy Hand Grenade, and you didn't even hit anything?!")


class CyberSword(Item):
    def __init__(self):
        super().__init__("Cyber Sword", "Cheatcode, Easter Egg, who's to say?")

    def use(self, player, location=None):
        player.strength = 99
        player.health = 99
        player.defense = 99


class Sunglasses(Item):
    def __init__(self):
        super().__init__("Sunglasses", "Life is about Balance, you gotta relax")

    def use(self, player, location=None):
        print("These could help you wind down in the right location")


# =============================================================================
# Character Classes
# =============================================================================

class Character:
    """Base class for all characters in the game."""

    def __init__(self, name, health, strength, defense, max_health):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.max_health = max_health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, amount):
        self.health = self.health - amount
        print(f'{self.name}-alot took {amount} damage, health now: {self.health}')

    def attack(self, target):
        this_roll = roll_d20()
        if this_roll > target.defense:
            target.take_damage(self.strength)
            print("Huzzah")
        else:
            print(f"{self.name}-alot's attack missed!")

    def __str__(self):
        return f"{self.name} (HP: {self.health}/{self.max_health})"


class Player(Character):
    """The player character."""

    def __init__(self, name):
        super().__init__(name, health=100, strength=5, defense=5, max_health=100)
        self.mana = 0
        self.inventory = []

    def pick_up(self, item):
        self.inventory.append(item)
        print(f"Picked up: {item.name}")

    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            for item in self.inventory:
                print(item)

    def use_item(self, item_name, location=None):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                item.use(self, location)
                self.inventory.remove(item)
                return
        print(f"You don't have a {item_name}.")


class Enemy(Character):
    """Base class for enemies."""

    def __init__(self, name, health=30, strength=2, defense=3, xp_value=10):
        super().__init__(name, health=health, strength=strength, defense=defense, max_health=health)
        self.xp_value = xp_value


class Giant(Enemy):
    def __init__(self):
        super().__init__("Mini_Math_Master", health=15, strength=5, defense=2, xp_value=50)
        self.loot = MudPie()
        self.ascii_art = r"""
       O
      /|\
     / | \
    /  |  \
   /   |   \
   --0-0---
   |      |
   |      |
   |______|
        """


class Goblin(Enemy):
    def __init__(self):
        super().__init__("MR_BRATWORST", health=5, strength=3, defense=5, xp_value=20)
        self.loot = MarketingMace()
        self.ascii_art = r"""
      /\
     /  \
    / >< \
   |0 __ 0|
   | |  | |
   | |  | |
   [======]
        """


class Zombie(Enemy):
    def __init__(self):
        super().__init__("Zombie", health=3, strength=2, defense=2, xp_value=5)
        self.loot = BusinessShield()
        self.ascii_art = r"""
     _____
    /     \
   |-@---@-|
   |  ___  |
   |______/
   /|   |\
  / |   | \
        """


class Ferret(Enemy):
    def __init__(self):
        super().__init__('Ferret with a Warrent', health=5, strength=10, defense=2, xp_value=1000)
        self.loot = HolyHandGrenade()
        self.ascii_art = r"""
    /\___/\
   (  o o  )
   (  =^=  )
    )     (
   (       )
  ( /\   /\ )
   ""   ""
        """


# =============================================================================
# Location Class
# =============================================================================

class Location:
    """A location in the game world."""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.enemies = []
        self.items = []

    def describe(self):
        """Print a full description of the location."""
        print(f"\n{'='*50}")
        print(f"  {self.name}")
        print(f"{'='*50}")
        print(self.description)
        if self.enemies:
            print(f"\nENEMIES:")
            for enemy in self.enemies:
                print(f"  - {enemy.name}")
        print(f"\nEXITS:")
        for direction, location in self.connections.items():
            print(f"  {direction} -> {location.name}")
        print(f"{'='*50}")

    def get_exits(self):
        """Return a list of available directions."""
        return list(self.connections.keys())

    def add_connection(self, direction, location):
        """Connect this location to another."""
        self.connections[direction] = location


# =============================================================================
# World Builder
# =============================================================================

def create_world():
    """Create and connect all locations. Returns the starting location."""

    The_Mountain = Location(
        "The Mountain",
        "A foggy mountain filled with Wonder, Horrors, and your greatest imagination"
    )

    The_Arena = Location(
        "The Arena",
        "A monument to competition, Graveyard to many, Glory to the Lucky"
    )

    The_Cyber_Cellar = Location(
        "CYBER CELLAR",
        "A pathway to untold riches, but at what cost?"
    )

    Zombie_College = Location(
        "Zombie College",
        "It's unclear if they ate all the brains... or if there were any here to begin with"
    )

    The_Beach = Location(
        "The Beach",
        "Well... That's it, doesn't get much better. Maybe the Joke is this is the end..."
    )

    # Connect locations (both ways)
    The_Mountain.add_connection("east", The_Arena)
    The_Arena.add_connection("west", The_Mountain)

    The_Mountain.add_connection("west", Zombie_College)
    Zombie_College.add_connection("east", The_Mountain)

    The_Arena.add_connection("below", The_Cyber_Cellar)
    The_Cyber_Cellar.add_connection("above", The_Arena)

    The_Cyber_Cellar.add_connection("east", The_Beach)
    The_Beach.add_connection("west", The_Cyber_Cellar)

    Zombie_College.add_connection("west", The_Beach)
    The_Beach.add_connection("east", Zombie_College)

    # Add enemies
    Zombie_College.enemies.append(Zombie())
    Zombie_College.enemies.append(Zombie())
    Zombie_College.enemies.append(Zombie())
    Zombie_College.enemies.append(Zombie())
    Zombie_College.enemies.append(Zombie())

    The_Arena.enemies.append(Giant())
    The_Arena.enemies.append(Giant())
    The_Arena.enemies.append(Goblin())

    The_Cyber_Cellar.enemies.append(Ferret())

    # Hidden Easter Egg
    The_Mountain.items.append(CyberSword())

    return The_Mountain


# =============================================================================
# Combat System
# =============================================================================

class Combat:
    """Manages turn-based combat between player and enemy."""

    PLAYER_TURN = "player_turn"
    ENEMY_TURN = "enemy_turn"
    COMBAT_END = "combat_end"

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.state = Combat.PLAYER_TURN
        self.combat_log = []

    def start(self):
        """Begin combat and run until someone wins/loses/flees."""
        print(f"\n⚔️ COMBAT BEGINS! ⚔️")
        print(f"{self.player.name} vs {self.enemy.name}!")
        if hasattr(self.enemy, 'ascii_art'):
            print(self.enemy.ascii_art)

        while self.state != Combat.COMBAT_END:
            if self.state == Combat.PLAYER_TURN:
                self.player_turn()
            elif self.state == Combat.ENEMY_TURN:
                self.enemy_turn()
        return self.get_result()


    def player_turn(self):
        """Handle player's turn in combat."""
        print(f"\n{self.player} | {self.enemy}")
        print("What do you do? (attack / run)")

        action = input("> ").lower().strip()

        if action == "attack":
            self.player.attack(self.enemy)
            if not self.enemy.is_alive():
                print(f"\n🎉 {self.enemy.name} has been defeated!")
                self.state = Combat.COMBAT_END
            else:
                self.state = Combat.ENEMY_TURN

        elif action == "run":
            if random.random() < 0.5:
                print("You successfully fled!")
                self.state = Combat.COMBAT_END
            else:
                print("Couldn't escape!")
                self.state = Combat.ENEMY_TURN

        else:
            print("Invalid action. Try 'attack' or 'run'.")

    def enemy_turn(self):
        """Handle enemy's turn in combat."""
        print(f"\n{self.enemy.name}'s turn...")
        self.enemy.attack(self.player)

        if not self.player.is_alive():
            print(f"\n💀 {self.player.name} has fallen!")
            self.state = Combat.COMBAT_END
        else:
            self.state = Combat.PLAYER_TURN

    def get_result(self):
        """Return the combat result: 'victory', 'defeat', or 'fled'."""
        if not self.enemy.is_alive():
            return "victory"
        elif not self.player.is_alive():
            return "defeat"
        else:
            return "fled"


# =============================================================================
# Main Game Class
# =============================================================================

class Game:
    """Main game controller."""

    EXPLORING = "exploring"
    IN_COMBAT = "in_combat"
    GAME_OVER = "game_over"
    VICTORY = "victory"

    def __init__(self):
        self.player = None
        self.current_location = None
        self.state = Game.EXPLORING
        self.game_running = True

    def start(self):
        """Initialize and start the game."""
        self.show_intro()
        self.create_player()
        self.current_location = create_world()
        self.current_location.describe()

        while self.game_running:
            if self.state == Game.EXPLORING:
                self.exploration_loop()
            elif self.state == Game.GAME_OVER:
                self.show_game_over()
                break
            elif self.state == Game.VICTORY:
                self.show_victory()
                break

    def show_intro(self):
        """Display the game introduction."""
        print("\n" + "="*60)
        print("         MYSTIC MOUNTAIN")
        print("="*60)
        print("\nYou look down from high atop a mountain in the north, As mist surrounds you...")
        print("Far in the Distance you see Hope! Water and sand in the distance! But before you lies great distance and foes.")
        print("\n" + "="*60)
        print(r"""   
                    🗾 MAP 🗾
              
                ⛰️  THE MOUNTAIN ⛰️
               /  (Start Here)   \
             west               east
            /                       \
🧟 ZOMBIE COLLEGE 🧟          ⚔️ THE ARENA ⚔️
[5 Zombies]     \              [2 Giants, 1 Goblin]
[Sunglasses       \                  |
 spawn here]     west              below
                   \                 |
                    \        🐀 CYBER CELLAR 🐀
                     \       [Ferret w/ a Warrant]
                      \            /
                       \         east
                        \        /
                     🏖️ THE BEACH 🏖️
                      ~~ VICTORY ~~
                    ._  .  ._  .  .
                   '  '  '  '  '  '
                  ~~~~~~~~~~~~~~~~~
                    🌴  YOU WIN  🌴
    """)


    def create_player(self):
        """Create the player character."""
        print("\nWhat is your name, brave traveler?")
        name = input("> ")
        self.player = Player(name)
        print(f"\nWelcome, {name}alot! Your adventure begins...")

    def exploration_loop(self):
        """Handle player input during exploration."""
        print("\nWhat do you do? (type 'help' for commands)")
        command = input("> ").lower().strip()

        parts = command.split()
        if not parts:
            return

        action = parts[0]

        if action == "help":
            self.show_help()

        elif action == "look":
            self.current_location.describe()

        elif action == "go" and len(parts) > 1:
            direction = parts[1]
            self.move(direction)

        elif action in ["north", "south", "east", "west", "up", "down", "below", "above"]:
            self.move(action)

        elif action in ["fight", "attack"]:
            self.initiate_combat()

        elif action in ["inventory", "i"]:
            self.player.show_inventory()

        elif action == "quit":
            print("Thanks for playing!")
            self.game_running = False

        elif action == "use" and len(parts) > 1:
            item_name = " ".join(parts[1:])
            self.player.use_item(item_name, self.current_location)

        elif action == "grab" or (action == "pick" and len(parts) > 1):
            if self.current_location.items:
                item = self.current_location.items.pop(0)
                self.player.pick_up(item)
            else:
                print("There's nothing to pick up here.")

        else:
            print("I don't understand that command. Type 'help' for options.")

    def move(self, direction):
        """Move the player in the specified direction."""
        if direction in self.current_location.connections:
            destination = self.current_location.connections[direction]
            if destination.name == "The Beach":
                has_key = any(item.name == "Sunglasses" for item in self.player.inventory)
                if not has_key:
                    print("The door to The Beach is locked! You need a pair of shades...")
                    return
                else:
                    print("You put on your shades and head to the beach...")
            self.current_location = destination
            self.current_location.describe()
            if self.current_location.enemies:
                self.initiate_combat()
        else:
            print(f"You can't go {direction} from here.")

    def initiate_combat(self):
        """Start combat with an enemy in the current location."""
        if self.current_location.name == "The Beach" and not self.current_location.enemies:
            self.state = Game.VICTORY
            return
        if not self.current_location.enemies:
            print("There's nothing to fight here.")
            return

        enemy = self.current_location.enemies[0]
        battle = Combat(self.player, enemy)
        result = battle.start()

        if result == "victory":
            self.current_location.enemies.remove(enemy)
            if hasattr(enemy, 'loot') and enemy.loot:
                print(f"\n{enemy.name} dropped: {enemy.loot.name}!")
                self.player.pick_up(enemy.loot)
            if self.current_location.name == "Zombie College" and not self.current_location.enemies:
                key = Sunglasses()
                self.current_location.items.append(key)
                print(f"\nFinally the path seems so clear... A pair of glowing {key.name} is just on the ground just in front of you")
        elif result == "defeat":
            self.state = Game.GAME_OVER

    def show_help(self):
        """Display available commands."""
        print("\n📜 AVAILABLE COMMANDS:")
        print("  go [direction] - Move in a direction (north, south, east, west, above, below)")
        print("  look           - Examine your surroundings")
        print("  fight          - Attack an enemy in this location")
        print("  grab           - Pick up an item from the ground")
        print("  use [item]     - Use an item from your inventory")
        print("  inventory      - Check your inventory")
        print("  help           - Show this help message")
        print("  quit           - Exit the game")

    def show_game_over(self):
        """Display game over message."""
        print("\n" + "="*60)
        print("                    GAME OVER")
        print("="*60)
        print("\nYou have fallen. The adventure ends here...")
        print("\n(But you can always try again!)")

    def show_victory(self):
        """Display victory message."""
        print("\n" + "="*60)
        print("                    🎉 VICTORY! 🎉")
        print("="*60)
        print("\nNow Get off the screen and Go Touch Grass")


# =============================================================================
# Run the Game
# =============================================================================

if __name__ == "__main__":
    game = Game()
    game.start()
# Game Design Document

## Theme / Setting
UUONDER, A dystopian fantasy with Giants, Goblins, a Ferret with a Warrant, and enough Monty Python lines to hopefully make it entertaining. The world is absurd, the enemies are a little ridiculous, but then again so am I.

## Player's Goal
Escape the Mystic Mountain and fight your way through enemies to reach the beast! Fight through hordes of Zombies to earn the key to surviving college,  prove yourself to your greatest critiques through battles with Giants and Goblins in The Arena, and survive the Ferret with a Warrant lurking in the Cyber Cellar. Only those cool enough to walk their own path will find their way to paradise. Get to The Beach, touch "grass", and win the game.

## Locations (4-6)
[List your locations and sketch how they connect]

```
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


    === LEGEND ===
    🧟 = Zombie Territory     ⚔️ = Combat Arena
    🐀 = Underground Lair     🏖️ = Final Destination
    ⛰️ = Starting Point       🔑 = Need Sunglasses to enter Beach

```

## Enemy Types
---

### Zombie (Minion)
  _____                     | Stat | Value |
/       \.                  | STR | 2 |
| x   x |                   | HP | 3 |
|  ___  |                   | DEF | 2 |
|______/                    | XP | 5 |
/|   |\                     | Loot | Business Shield |
/|   | \                    | Location | Zombie College (x5) |
The undead student body of Zombie College. Most of them are dead, although you cant tell behind the Sunglasses...

### MR_BRATWORST (Elite)

   /\               | Stat | Value |
  /  \              | HP | 5 |
 / >< \             | STR | 3 |
|0 __ 0|            | DEF | 5 |
| |  | |            | XP | 20 |
| |  | |            | Loot | Marketing Mace |
[======]            | Location | The Arena |

An armour plated cone on his head, this goblin has a chip on his shoulder and surprisingly good defense. What he lacks in power, he makes up for in sheer stubbornness. Drops the Marketing Mace | Now you have their attention, but what are you going to do with it?

### Mini_Math_Master

   O                | Stat | Value |
  /|\               | HP | 15 |
 / | \              | STR | 5 |
/  |  \             | DEF | 2 |
/  |   \            | XP | 50 |
--0-0---            | Loot | Mud Pie |
|      |            | Location | The Arena (x2) |
|      |
|______|
A towering giant who hits like a freight train but can't defend himself. Lurks in The Arena doing trigonometry for fun. High health and high damage make him the tankiest regular enemy in the game. Drops a Mud Pie, because there's a lesson in there about taking L's.

### Ferret with a Warrant (BOSS)
    /\___/\         | Stat | Value |
   (  o o  )        | HP | 5 |
   (  =^=  )        | STR | 10 |
    )     (         | DEF | 2 |
   (       )        | XP | 1000 |
  ( /\   /\ )       | Loot | Holy Hand Grenade |
   ""   ""          | Location | Cyber Cellar |
The final gatekeeper of the Cyber Cellar. This ferret hits harder than anything else in the game with a devastating 10 strength. Drops the legendary Holy Hand Grenade, A weapon that can turn even a baron wasteland into sunshine and rainbows.

## Win Condition
Reach the beach with the secret key in order to unlock paradise (Sunglasses). You can find them by clearing "Zombie College" of brain eating students. Defeating the Ferret that defends the cyber cellar may help you find a relic to help you with that...

## Lose Condition
Your health reaches 0 during combat. No respawns, No second chances. If your die it's GAME OVER. Pick your fights carefully.

## Class Hierarchy
### Class Hierarchy
```
Character (base class)
│   Attributes: name, health, max_health, strength, defense
│   Methods: is_alive(), take_damage(), attack(), __str__()
│
├── Player(Character)
│     Attributes: mana, inventory
│     Methods: pick_up(), show_inventory(), use_item()
│
└── Enemy(Character)
      Attributes: xp_value, loot
    │
    ├── Zombie(Enemy)         — Minion, weak but numerous
    ├── Goblin(Enemy)         — Elite, high defense
    ├── Giant(Enemy)          — Elite, high HP and strength
    └── Ferret(Enemy)         — Boss, glass cannon

Item (base class)
│   Attributes: name, description
│   Methods: use(), __str__()
│
├── MudPie(Item)              — Heals 25 HP
├── BusinessShield(Item)      — +3 DEF, +5 STR
├── MarketingMace(Item)       — +5 STR
├── HolyHandGrenade(Item)     — Clears all enemies in a location
├── CyberSword(Item)          — Sets all stats to 99 (Easter Egg)
└── Sunglasses(Item)          — Key to unlock The Beach

Location
│   Attributes: name, description, connections, enemies, items
│   Methods: describe(), get_exits(), add_connection()

Combat
│   Attributes: player, enemy, state, combat_log
│   Methods: start(), player_turn(), enemy_turn(), get_result()

Game
    Attributes: player, current_location, state, game_running
    Methods: start(), show_intro(), create_player(), exploration_loop(),
             move(), initiate_combat(), show_help(), show_game_over(),
             show_victory()
```

## Additional Notes
[Any other design decisions, ideas, or plans]

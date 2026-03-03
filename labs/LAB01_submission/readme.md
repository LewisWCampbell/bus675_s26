# UUonder a Game by Lewis Campbell

## Story
You awaken atop a fog-covered mountain with nothing but your name and your fists. You can hear the roar's and shrieks of enemies close by, but in the distance you make out a shimmer of water and sand. THE BEACH, "Huzzah!" your way through Giants, Goblins, Zombies, and even a Ferret. Collect loot, use ancient relics, and fight your way to Paradise!

## How to Play

    **Movement:**
- `go [direction]` — Move to a connected location (e.g., `go east`, `go west`, `go below`, `go above`)
- You can also just type the direction: `east`, `west`, `below`, `above`

    **Combat:**
- `fight` or `attack` — Start a fight with an enemy in your current location
- During combat, type `attack` to swing or `run` to attempt escape (50% chance)
- Combat uses a d20 dice system — roll high to hit, roll low and you miss

    **Items:**
- `grab` — Pick up an item from the ground
- `use [item name]` — Use an item from your inventory (e.g., `use mud pie`, `use holy hand grenade`)
- `inventory` or `i` — Check what you're carrying

    **Other:**
- `look` — Re-examine your current location (enemies, exits)
- `help` — Show all available commands
- `quit` — Exit the game


### Running the Game
```bash
python game.py
```

### Commands
| `go [direction]` | Move to a connected location (east, west, above, below) |
| `east/west/above/below` | Shortcut — move without typing "go" |
| `look` | Re-examine your current location |
| `fight` or `attack` | Start combat with an enemy here |
| `attack` (in combat) | Swing at the enemy (d20 roll vs defense) |
| `run` (in combat) | 50% chance to flee combat |
| `grab` | Pick up an item from the ground |
| `use [item name]` | Use an item from your inventory |
| `inventory` or `i` | View your inventory |
| `help` | Show available commands |
| `quit` | Exit the game |


## Goal
### Goal:
Fight your way down the Mountain to The Beach. There are two paths to paradise, but both require the Sunglasses, the only key that unlocks The Beach. To earn them, you must clear all 5 Zombies from Zombie College. Once the last Zombie falls, the Sunglasses appear. Grab them, find your way to The Beach, and touch grass to win the game.

## Tips
There are rumors that an anctient artifact exists, guarded by a Prehistoric Ferret, Forged by the funniest of comedy acts. Could help to clear a lot of enemies quickly...

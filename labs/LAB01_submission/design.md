# Game Design Document

## Theme / Setting
[What's your theme? Fantasy, sci-fi, horror, action movie, etc.?]

## Player's Goal
[What does the player need to accomplish to win?]

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

## Enemies (2-4 types)
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

## Win Condition
[How does the player win?]

## Lose Condition
[How does the player lose?]

## Class Hierarchy
[Sketch your class design]

```
Character (base class)
├── Player
└── Enemy
    ├── ...
    └── ...

Location

Game
```

## Additional Notes
[Any other design decisions, ideas, or plans]

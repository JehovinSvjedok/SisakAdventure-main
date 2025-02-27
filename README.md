<<<<<<< HEAD
# Sisak Adventure

## Overview
This project is a card-based roguelike game inspired by "Slay the Spire". Players will navigate through various screens to select characters, edit their decks, and engage in gameplay.

## Project Structure
```
my-pygame-game
├── src
│   ├── main.py                # Entry point of the game
│   ├── screens                # Contains different game screens
│   │   ├── start_screen.py    # Start screen functionality
│   │   ├── choose_player_screen.py # Character selection screen
│   │   ├── tavern_screen.py    # Tavern for editing cards
│   │   └── gameplay_screen.py   # Main gameplay loop
│   ├── assets                  # Game assets
│   │   ├── images              # Image files (backgrounds, sprites, etc.)
│   │   └── sounds              # Sound files (music, effects)
│   └── utils                  # Utility functions
│       └── helpers.py         # Helper functions for various tasks
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```


## Files Description

- **Start.py**: The entry point of the game. Displays the start screen and navigates to the player selection screen.
- **biranje_igraca.py**: Handles the player selection screen where the user can choose a character.
- **glavna.py**: Contains the main game logic where the character can move left and right.
- **glavna2.py**: Another main game file with additional features such as entering a house or portal.
- **kuca.py**: Represents the house screen where the user can swap cards.
- **portal.py**: Represents the portal screen where the user can interact with circles.
- **test.py**: A test file for loading and displaying character characteristics.
- **saved_hand.json**: A JSON file that stores the saved hand of cards.
- **Slike/**: A directory containing images and music used in the game.

## Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/my-pygame-game.git

## Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/my-pygame-game.git
   ```
2. Navigate to the project directory:
   ```
   cd my-pygame-game
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Gameplay Mechanics
- **Start Screen**: Players can start the game and navigate to the character selection screen.
- **Choose Player Screen**: Players select their character from a list of available options.
- **Tavern Screen**: Players can edit their selected cards and manage their deck.
- **Gameplay Screen**: The main game loop where players encounter enemies and progress through the game.

## Contributing
Feel free to submit issues or pull requests if you would like to contribute to the project. 

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
=======
>>>>>>> 02a25cb72fe52cec8076667b1ce05b74d3cb43a0
>>>>>>
>>>>>>
UML Diagram For The Game
![UML](https://github.com/user-attachments/assets/7e317674-8cf3-41d0-acad-3bd6f491e1d1)

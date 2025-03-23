# Snake Game

A simple Snake game implemented using Python and Pygame. This project demonstrates a clean, modular structure by separating the game logic into multiple files and organizing code within a `src` folder.

## Project Structure

snake_game/
├── main.py
└── src/
   ├── init.py       # (makes src a package, can be empty)
   ├── settings.py       # Game settings and configuration
   ├── snake.py          # Snake class implementation
   ├── food.py           # Food class implementation
   └── game.py           # Main game logic and event handling


## Prerequisites

- **Python 3.x**
- **Pygame**: To install Pygame, run:

  ```bash
  pip install pygame
  ```

Installation
	1.	Clone or download the repository.
	2.	Navigate to the project folder:
    ```bash
    cd snake_game
    ```

	3.	Install the necessary Python dependencies as described in the Prerequisites.

Running the Game

To start the game, run:
```bash
python main.py
```
Use the arrow keys to control the snake. The goal is to eat the food, grow longer, and avoid collisions with the walls or yourself.

Features
	•	Modular Code Structure: Code is organized into separate modules in the src folder for maintainability and scalability.
	•	Simple Game Mechanics: Basic collision detection, score tracking, and snake growth.
	•	Asset Organization: External assets (images and sounds) can be placed in the assets folder.

Future Enhancements
	•	Adding a scoring system display on the game screen.
	•	Including sound effects and background music.
	•	Enhancing the graphics and adding animations.
	•	Implementing additional game modes or difficulty levels.

License

This project is licensed under the MIT License.

Acknowledgments
	•	This project uses Pygame for game development.

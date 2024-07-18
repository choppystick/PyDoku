# Sudoku Game with Python and Pygame

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [How to Play](#how-to-play)
6. [Project Structure](#project-structure)
7. [Code Overview](#code-overview)
8. [Future Enhancements](#future-enhancements)
9. [Contributing](#contributing)
10. [License](#license)

## Introduction

This project is an implementation of the classic Sudoku puzzle game using Python and Pygame. It offers a graphical user interface for playing Sudoku, with features such as a menu system, difficulty levels, and the ability to play puzzles from the New York Times website.

## Features

- Graphical user interface built with Pygame
- Main menu with options to start a new game or exit
- Ability to play randomly generated Sudoku puzzles
- Option to play Sudoku puzzles from the New York Times website
- Three difficulty levels for NYT puzzles: Easy, Medium, and Hard
- Interactive gameplay with mouse and keyboard input
- Automatic validation of completed puzzles

## Requirements

- Python 3.7+
- Pygame
- Requests library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/sudoku-game.git
   cd sudoku-game
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install pygame requests
   ```

4. Run the game:
   ```
   python main.py
   ```

## How to Play

1. Launch the game by running `main.py`.
2. In the main menu, you can choose to:
   - Play a randomly generated Sudoku puzzle
   - Play a puzzle from the New York Times (with difficulty selection)
   - Exit the game
3. During gameplay:
   - Click on a cell to select it
   - Use number keys (1-9) to input a number into the selected cell
   - Press ESC to return to the main menu
4. The game will automatically validate your solution when the board is filled.

## Project Structure

The project is structured into several Python classes:

- `SudokuBoard`: Represents the Sudoku board and handles puzzle generation and validation
- `SudokuGame`: Manages the game state and user interactions
- `SudokuRenderer`: Handles the drawing of the Sudoku board on the screen
- `Menu`: Manages the main menu and NYT difficulty selection menu
- `GameController`: Orchestrates the overall game flow

## Code Overview

### SudokuBoard

This class is responsible for generating and managing the Sudoku board. It includes methods for:
- Generating a new Sudoku puzzle
- Validating moves
- Fetching puzzles from the New York Times website

### SudokuGame

This class manages the game state, including:
- Starting a new game
- Handling user input (cell selection and number input)
- Checking if the puzzle is completed

### SudokuRenderer

This class is responsible for drawing the Sudoku board on the screen, including:
- Drawing the grid
- Rendering numbers
- Highlighting the selected cell

### Menu

This class manages the menu system, including:
- Drawing the main menu and NYT difficulty selection menu
- Handling button clicks

### GameController

This class orchestrates the overall game flow, managing transitions between the menu and gameplay states.

## Future Enhancements

- Add a scoring system
- Improve graphics and add animations
- Add sound effects and background music
- Implement the LP solver but I honestly I have o idea how.

## Contributing

Contributions to this project are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enjoy playing PyDoku! If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository.

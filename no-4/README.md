# CONNECT4

## Project Description
This Python project implements a classic Connect4 game for two players. Players take turns dropping discs into a 6x7 board, aiming to align four consecutive discs either vertically, horizontally, or diagonally. The project demonstrates game logic implementation, user interaction, and win condition checks in a grid-based game.

## Files
- `connect4.py`: The main Python script that runs the Connect4 game.

## Usage
1. **Run the script**:
   ```bash
   python connect4.py
   ```
## Play the Game

- **Players take turns** entering a column number (1-7) to drop their disc.
- The game will **display the updated board** after each move.
- The **first player to align four of their discs** in any direction wins the game.

## Follow the Prompts

- **Enter a column number** to place your disc on the board.
- **Watch the board update** as discs are placed in the lowest available position in the chosen column.
- The game ends when one player successfully aligns four discs in a row, and the winner is announced.
## What I Learned

- **Game Logic Implementation**: I developed the logic required to simulate a Connect4 game, including checking for vertical, horizontal, and diagonal win conditions.
- **Board Management**: I learned how to manage a 2D list to represent the game board and update it based on player actions.
- **User Interaction**: The project required handling user inputs to simulate real-time gameplay between two players.
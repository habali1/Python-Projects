# 2048

## Project Description
This Python project implements a simplified version of the popular 2048 game. Players slide numbered tiles on a 4x4 grid using "left," "right," "up," and "down" commands. The goal is to combine tiles to create a tile with the number 2048. The game ends when no more moves are possible.

## Files
- `2048.py`: The main Python script that contains the implementation of the 2048 game.

## Usage
1. **Run the script**:
   ```bash
   python 2048.py
   ```
## Play the Game

- Use the **"left," "right," "up," and "down"** commands to slide the tiles.
- The game will generate new tiles with a value of **2 or 4** after each move.
- The game ends when no more moves are possible or when you create a tile with the number **2048**.
## What I Learned

- **Game Logic Implementation**: I deepened my understanding of game development by implementing the core mechanics of the 2048 game, including tile movement, combination, and win/loss conditions.
- **Randomization and Probability**: I applied randomization techniques to generate new tiles with specific probabilities (60% for 2s and 40% for 4s), enhancing the game's realism.
- **Recursive Error Handling**: I learned to manage and handle `RecursionError` in Python, particularly in the context of game termination when no more valid moves are available.

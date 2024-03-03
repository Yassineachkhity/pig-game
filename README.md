# pig-game
This is a simple command-line dice game implemented in Python. The game is designed for 2 to 4 players, where each player takes turns rolling a six-sided die. The objective of the game is to be the first player to reach a total score of 50 or more.

## How to Play

1. Run the Python script `pig.py`.
2. Enter the number of players (2 to 4) when prompted.
3. Each player takes turns rolling the die by typing 'y' for yes or 'n' for no.
4. If a player rolls a 1, their turn ends and they lose all points accumulated during that turn.
5. The game continues until one player reaches a total score of 50 or more.
6. The player with the highest score at the end of the game is declared the winner.

## Functionality

- The `roll()` function simulates rolling a six-sided die and returns the result.
- The `get_num_players()` function prompts the user to enter the number of players and ensures it is within the valid range (2 to 4).
- The `player_turn(player_idx)` function handles the turn for each player, allowing them to roll the die and accumulate points until they decide to stop or roll a 1.
- The `main()` function orchestrates the game by initializing player scores, executing player turns, and determining the winner.

## Dependencies

This game requires Python 3 to run.

## Usage

To play the game, simply run the `pig.py` script in your Python environment. Follow the on-screen instructions to enter the number of players and take turns rolling the die.

## Author

This game was created by ACHKHITY YASSINE.

# Tic-Tac-Toe AI - Multiagent Search

This project is part of Homework 2 for the course **CSE 5120: Introduction to Artificial Intelligence** at California State University, San Bernardino. The goal is to implement a **multi-agent Tic-Tac-Toe game** using the **Minimax** algorithm and its variant **Negamax**, with optional **Alpha-Beta pruning**. The game allows for human vs. computer play on a configurable board size.

## Project Overview

The game explores adversarial search algorithms in the context of a zero-sum, fully observable two-player game. The human player competes against the AI (computer) on a larger Tic-Tac-Toe board, where both attempt to create the most triplets of matching symbols.

### Features
- **Configurable Board Size**: Play on a board ranging from 3x3 to 5x5 (or larger depending on your system's capacity).
- **Human vs. AI**: The human player moves first, followed by the AI, which calculates its moves using the Minimax or Negamax algorithms.
- **Minimax with Alpha-Beta Pruning**: The AI uses Minimax (or Negamax) with optional Alpha-Beta pruning to make the game more efficient.
- **Graphical Interface with `pygame`**: A simple graphical interface is created using the `pygame` library.

## File Structure

| File Name                | Description |
|--------------------------|-------------|
| `multiAgents.py`          | Implements the Minimax and Negamax agents for adversarial search. |
| `large_board_tic_tac_toe.py` | The main file that runs the game, including the `pygame` GUI code for configuring board size and playing the game. |
| `GameStatus_5120.py`      | Handles game logic such as checking terminal states, calculating scores, and generating valid moves. |

## Algorithms

### Minimax Algorithm
Minimax is used to simulate all possible moves and determine the optimal strategy by maximizing the player's score and minimizing the opponent's score. 

### Negamax Algorithm
Negamax is a variant of Minimax that simplifies code implementation by using a single function for both players, as the value of a move for one player is the negative of the value for the opponent.

### Alpha-Beta Pruning
This technique is used to optimize the Minimax algorithm by pruning branches in the search tree that don't need to be evaluated.

## How to Run

### Requirements
- Python 3.x
- `pygame` library (install via `pip install pygame`)

### Running the Game

```bash


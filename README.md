# Tic-Tac-Toe AI - Multiagent Search

This project is an implementation of a **multi-agent Tic-Tac-Toe game** as part of Homework 2 for the course **CSE 5120: Introduction to Artificial Intelligence** at California State University, San Bernardino. The game is built using the **Minimax** algorithm and its variant **Negamax** with optional Alpha-Beta pruning. The game is designed to be played on a configurable board size, and the computer AI competes against a human player.

## Project Overview

This project is a classic example of **deterministic, turn-based, zero-sum games**. It uses adversarial search algorithms to implement an intelligent computer opponent in the game of Tic-Tac-Toe. The human player and computer alternate turns, and the winner is determined based on who manages to create the most winning triplets of symbols (X or O).

### Features
- **Customizable Board Size**: Play on 3x3, 4x4, 5x5 boards, or larger.
- **Human vs. AI**: The human player always moves first, followed by the AI opponent.
- **Minimax with Alpha-Beta Pruning**: The AI uses Minimax (or Negamax) with optional Alpha-Beta pruning to efficiently explore the game tree and select the optimal move.
- **Graphical Interface**: The game is rendered using `pygame`, providing an intuitive interface for human vs. AI gameplay.

## File Structure

The project consists of the following files:

| File Name                | Description |
|--------------------------|-------------|
| `multiAgents.py`          | Implements the Minimax and Negamax agents for adversarial search. This file contains the logic for the AI opponent. |
| `large_board_tic_tac_toe.py` | Main file that runs the game. This file includes the **pygame** GUI code, allowing the player to select the board size, reset the game, and view the score. |
| `GameStatus_5120.py`      | Handles the game logic, including checking for terminal states, generating valid moves, and calculating the score. |

## Algorithms

### Minimax Algorithm
Minimax is a decision-making algorithm that is used in adversarial games. In this game, the Minimax algorithm works by simulating all possible moves and selecting the move that maximizes the player's chance of winning, while minimizing the opponent's score.

**Key Functions**:
- `minimax`: Implements the Minimax algorithm with optional Alpha-Beta pruning.
- `max_value` and `min_value`: Recursive functions that explore the game tree to determine the best move for the human and computer players, respectively.

### Negamax Algorithm
Negamax is a simplification of the Minimax algorithm. It exploits the zero-sum property of the game, allowing the same function to be used for both maximizing and minimizing player actions.

**Key Functions**:
- `negamax`: A variation of Minimax where the score of one player is the negative score of the other player.

### Alpha-Beta Pruning
This is an optimization technique for the Minimax algorithm. Alpha-Beta pruning reduces the number of nodes that are evaluated in the game tree, improving the efficiency of the algorithm by pruning branches that do not affect the final decision.

## How to Run

### Requirements
- Python 3.x
- `pygame` library

You can install `pygame` via pip:
```bash
pip install pygame

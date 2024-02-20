# Tic-Tac-Toe with Minimax Algorithm
This simple console-based and browser game allows you to play a Tic-Tac-Toe game against an AI opponent that uses the Minimax algorithm to make strategic moves.

## Features
Player vs. AI gameplay with Minimax algorithm. <br/>
Command-line or browser interface for ease of use. <br/>
Minimalistic design for quick and straightforward gameplay.

## Minimax Algorithm
The Minimax algorithm is a decision-making algorithm used in two-player games, such as Tic-Tac-Toe. It is used to determine the best possible move for a player, <br/>
assuming that the opponent is also playing optimally. The algorithm works by recursively exploring all possible moves in the game tree and assigning a score to each move. <br/>
The player chooses the move with the highest score (for maximizing player) or the lowest score (for minimizing player) at each level of the tree. <br/>
This process continues until a terminal state (win, loss, or draw) is reached, and the algorithm returns the best move.

## Running the game with Command-line interface.
1. Clone repository.
2. Run the game with: 'python game.py'

## Running the game with browser interface.
1. Clone repository.
2. Install node.js (nodejs.org).
3. Run 'npm install' in frontend directory to install react dependencies.
4. Run 'npm start' in frontend directory to start frontend server.
5. Run 'pip install -r requirements.txt'
6. Run 'uvicorn backend.main:app' on base directory to start backend server.
7. Play.

## Game Instructions
Use the numbers 1-9 (command-line) or click on the box (browser) to make a move on the Tic-Tac-Toe board. <br/>
The game will prompt you to enter your move during your turn. <br/>
The AI opponent will use the Minimax algorithm to make its moves.

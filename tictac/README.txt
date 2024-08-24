Explanation of the Code
Tkinter: A built-in Python library used for creating graphical user interfaces. Here, we use it to create buttons for each cell on the Tic-Tac-Toe board, as well as labels and buttons for game control.

Board Representation: The game board is represented as a list of 9 elements (board), where each element corresponds to a cell in the 3x3 grid. The buttons list holds the Tkinter buttons, allowing us to update the GUI based on the game state.

Minimax Algorithm: This is the same as the previous implementation, used to determine the best move for the AI. It remains unchanged.

Button Click Handling (click_button): When a player clicks a button, the game checks if the move is valid, updates the board, and checks for a win or draw. If the game isn't over, the AI makes its move.

GUI Elements:

Buttons: Represent the Tic-Tac-Toe board cells. Clicking a button makes the player's move.
Labels: Display messages like "You win!" or "AI wins!".
Restart Button: Resets the game to start a new match.
Symbol Choice: At the start of the game, the player chooses whether to play as X or O. The game then switches to the main board view.

Restarting the Game: The restart_game function clears the board and re-enables the buttons for a new game.

Algorithm Used
Minimax Algorithm:

Purpose: The Minimax algorithm is a decision-making algorithm used in game theory to find the optimal move for a player, assuming that the opponent also plays optimally. It’s commonly used in turn-based games like Tic-Tac-Toe.
How It Works:
Game Tree: The algorithm simulates all possible moves by creating a game tree, where each node represents a possible game state.
Recursion: It evaluates each move recursively, with two main cases:
Maximizing: If it's the AI's turn, the algorithm picks the move with the highest score.
Minimizing: If it's the human player's turn, the algorithm picks the move with the lowest score.
Scoring:
+1 if the AI wins.
-1 if the human player wins.
0 if it’s a draw.
Base Cases: The recursion stops when a win, loss, or draw is detected, returning the corresponding score.
Alpha-Beta Pruning:

Purpose: Alpha-Beta Pruning is an optimization technique for the Minimax algorithm. It reduces the number of nodes that are evaluated by "pruning" branches that don’t need to be explored, thereby speeding up the decision-making process.

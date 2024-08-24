import tkinter as tk
import math

# Constants
EMPTY = " "
HUMAN = None
AI = None
board = [EMPTY] * 9

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create a list of buttons corresponding to the board
buttons = []

def print_board_gui():
    """Update the GUI board based on the current state."""
    for i in range(9):
        buttons[i]["text"] = board[i]

def is_winner(board, player):
    """Check if the given player has won the game."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # vertical
        [0, 4, 8], [2, 4, 6]             # diagonal
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def is_draw(board):
    """Check if the game is a draw."""
    return EMPTY not in board

def minimax(board, depth, is_maximizing, alpha, beta, ai_player, human_player):
    """The Minimax algorithm with Alpha-Beta Pruning."""
    if is_winner(board, ai_player):
        return 1
    elif is_winner(board, human_player):
        return -1
    elif is_draw(board):
        return 0
    
    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = ai_player
                eval = minimax(board, depth + 1, False, alpha, beta, ai_player, human_player)
                board[i] = EMPTY
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = human_player
                eval = minimax(board, depth + 1, True, alpha, beta, ai_player, human_player)
                board[i] = EMPTY
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def best_move(board, ai_player, human_player):
    """Determines the best move for the AI."""
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = ai_player
            move_val = minimax(board, 0, False, -math.inf, math.inf, ai_player, human_player)
            board[i] = EMPTY
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

def click_button(i):
    """Handle button clicks by the player."""
    global board
    if board[i] == EMPTY:
        board[i] = HUMAN
        print_board_gui()
        if is_winner(board, HUMAN):
            result_label.config(text="You win!")
            disable_buttons()
            return
        elif is_draw(board):
            result_label.config(text="It's a draw!")
            return

        # AI makes its move
        move = best_move(board, AI, HUMAN)
        board[move] = AI
        print_board_gui()

        if is_winner(board, AI):
            result_label.config(text="AI wins!")
            disable_buttons()
        elif is_draw(board):
            result_label.config(text="It's a draw!")

def disable_buttons():
    """Disable all buttons after the game ends."""
    for button in buttons:
        button.config(state=tk.DISABLED)

def restart_game():
    """Reset the board and start a new game."""
    global board
    board = [EMPTY] * 9
    for button in buttons:
        button.config(state=tk.NORMAL)
    print_board_gui()
    result_label.config(text="")

def choose_symbol(symbol):
    """Allow the player to choose their symbol (X or O)."""
    global HUMAN, AI
    HUMAN = symbol
    AI = "O" if HUMAN == "X" else "X"
    choice_frame.pack_forget()  # Hide the choice buttons
    game_frame.pack()           # Show the game board

# Create the GUI components

# Frame for the game board
game_frame = tk.Frame(root)
game_frame.pack()

# Create and place the buttons
for i in range(9):
    button = tk.Button(game_frame, text=EMPTY, font=("Arial", 24), width=5, height=2,
                       command=lambda i=i: click_button(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Frame for symbol choice
choice_frame = tk.Frame(root)
choice_frame.pack()

# Buttons for choosing the symbol
tk.Label(choice_frame, text="Choose your symbol:", font=("Arial", 16)).pack()
tk.Button(choice_frame, text="X", font=("Arial", 16), command=lambda: choose_symbol("X")).pack(side=tk.LEFT, padx=10)
tk.Button(choice_frame, text="O", font=("Arial", 16), command=lambda: choose_symbol("O")).pack(side=tk.LEFT, padx=10)

# Label for displaying the result
result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack()

# Restart button
restart_button = tk.Button(root, text="Restart", font=("Arial", 16), command=restart_game)
restart_button.pack()

# Start the Tkinter event loop
root.mainloop()

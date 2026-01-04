# Tic Tac Toe AI

# Random Module
import random

# Display board
def display_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()

# Function for defining win condition     
def check_winner(board, current_player):
    winning_combos = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],    # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],    # Columns
    [0, 4, 8], [2, 4, 6]                # Diagonals
    ]

    return any(all(board[i] == current_player for i in condition) for condition in winning_combos)

# Function for defining draw condition
def check_draw(board):
    return all(space != ' ' for space in board)

# Function for AI to choose random move
def ai_move(board):
    available_moves = [i for i, space in enumerate(board) if space == ' ']
    return random.choice(available_moves)

# Definitions
restart = 'Y'

while restart != 'N':

    # Definitions
    game_over = False
    board = [' ' for _ in range(9)]
    # Indexes: 0  1  2
    #          3  4  5
    #          6  7  8

    # Welcome!
    #print("Welcome to Tic-Tac-Toe!")

    # current_player = input("Please choose X or O: ").upper()

    # while current_player not in ['X', 'O']:
    #     current_player = input("Please choose X or O: ").upper()

    current_player = 'X'

    print(f"The player is {current_player}.")

    print(f"{current_player} will start.")

    # Starting Board
    print()
    print(" 1 | 2 | 3")
    print("---|---|---")
    print(" 4 | 5 | 6")
    print("---|---|---")
    print(" 7 | 8 | 9")
    print()

    # While Loop for running the game and checking win/draw condition
    while not game_over:
        
        # Human Player Turn
        if current_player == 'X':
            position = input("Choose a position (1-9): ")

            # Input Validation
            while not position.isdigit() or int(position) not in range(1, 10):
                position = input("Choose a position (1-9): ")

            # Input check for occupied position
            if board[int(position) - 1] != ' ':
                position = input("That position is already occupied, please choose another position (1-9): ")
                while not position.isdigit() or int(position) not in range(1, 10):
                    position = input("Choose a position (1-9): ")

            # Convert position(str) to position(int)
            position = int(position)

            # Place mark
            board[position - 1] = current_player

        # AI Turn
        else:
            position = ai_move(board)
            while board[int(position) - 1] != ' ':
                position = ai_move(board)
            board[position - 1] = current_player

        # Clear Screen
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

        print("AI's turn...")

        # Print board
        display_board(board)

        # Check win condition
        if check_winner(board, current_player):
            os.system('cls' if os.name == 'nt' else 'clear')
            display_board(board)
            print(f"{current_player} wins!")
            game_over = True

        # Check draw condition
        elif check_draw(board):
            os.system('cls' if os.name == 'nt' else 'clear')
            display_board(board)
            print("It's a tie!")
            game_over = True

        # Switch player
        else:
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

    # Ask for restart
    restart = input("Would you like to restart [Y / N]: ").upper()
    if restart == 'N':
        print("Thank you for playing Tic Tac Toe!")
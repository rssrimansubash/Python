import random

def analyze_board(board):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != 0:
            return board[combo[0]]
    if 0 not in board:
        return -1
    return 0

def print_board(board):
    symbols = [' ', 'X', 'O']
    for i in range(3):
        print(f"{symbols[board[i * 3]]} | {symbols[board[i * 3 + 1]]} | {symbols[board[i * 3 + 2]]}")
        if i < 2:
            print("--+---+--")

def computer_move(board):
    empty_indices = [i for i in range(9) if board[i] == 0]
    return random.choice(empty_indices)

def main():
    print("Welcome to Tic-Tac-Toe!")
    choice = int(input("Enter 1 to play against a Computer or 2 to play against another Player: "))
    board = [0] * 9
    print("Positions are as follows:")
    print("1 | 2 | 3\n--+---+--\n4 | 5 | 6\n--+---+--\n7 | 8 | 9")
    if choice == 1:
        print("Computer: O vs Player: X")
        player_turn = int(input("Enter 1 to play first or 2 to play second: "))
        for i in range(9):
            print_board(board)
            if (i % 2 == 0 and player_turn == 1) or (i % 2 == 1 and player_turn == 2):
                move = int(input("Enter your move (1-9): ")) - 1
                if board[move] == 0:
                    board[move] = 1
                else:
                    print("Invalid move! Try again.")
                    continue
            else:
                print("Computer's turn...")
                move = computer_move(board)
                board[move] = 2
            result = analyze_board(board)
            if result == 1:
                print_board(board)
                print("Player wins!")
                break
            elif result == 2:
                print_board(board)
                print("Computer wins!")
                break
            elif result == -1:
                print_board(board)
                print("It's a draw!")
                break
    elif choice == 2:
        print("Player 1: X and Player 2: O")
        for i in range(9):
            print_board(board)
            move = int(input(f"Player {1 if i % 2 == 0 else 2}, enter your move (1-9): ")) - 1
            if board[move] == 0:
                board[move] = 1 if i % 2 == 0 else 2
            else:
                print("Invalid move! Try again.")
                continue
            result = analyze_board(board)
            if result == 1:
                print_board(board)
                print("Player 1 wins!")
                break
            elif result == 2:
                print_board(board)
                print("Player 2 wins!")
                break
            elif result == -1:
                print_board(board)
                print("It's a draw!")
                break
    else:
        print("Invalid choice! Exiting...")

if __name__ == "__main__":
    main()
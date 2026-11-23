import random

def print_board(board):
    print()
    print("-------------")
    for i in range(3):
        print("|", board[i*3], "|", board[i*3+1], "|", board[i*3+2], "|")
        print("-------------")

def check_winner(board, symbol):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for combo in winning_combinations:
        if all(board[i] == symbol for i in combo):
            return True

    return False

def play_game():
    board = [" " for _ in range(9)]

    print("\n=== TIC-TAC-TOE ===")
    print("You are X | Computer is O")

    while True:
        print_board(board)

        # Player's move
        try:
            move = int(input("Choose a position (1-9): ")) - 1

            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move! Try again.")
                continue

        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue

        board[move] = "X"

        if check_winner(board, "X"):
            print_board(board)
            print("🎉 Congratulations! You Win!")
            break

        if " " not in board:
            print_board(board)
            print("It's a Draw!")
            break

        # Computer's move
        computer_moves = [i for i in range(9) if board[i] == " "]
        computer_move = random.choice(computer_moves)

        board[computer_move] = "O"
        print("\nComputer played!")

        if check_winner(board, "O"):
            print_board(board)
            print("Computer Wins! Try Again.")
            break

        if " " not in board:
            print_board(board)
            print("It's a Draw!")
            break

def main():
    while True:
        play_game()

        again = input("\nPlay again? (y/n): ").lower()

        if again != "y":
            print("Thanks for playing! 👋")
            break

main()
from random import randint

# Create a table which will use as an ocean.
board = []

for x in range(4):
    board.append(["O"] * 4)


def print_board(board):
    for row in board:
        print(" ".join(row))


# Here we generate a random coordinate for the ship in the ocean.
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)


# The player has the right to guess 4 times.
for turn in range(4):
    print("Turn", turn + 1)
    guess_row = int(input("Guess Row: ")) - 1
    guess_col = int(input("Guess Col: ")) - 1

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    else:
        if guess_row not in range(4) or guess_col not in range(4):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        
        if (turn == 3):
            print("Game Over!")

        print_board(board)

# Print correct answer.
print("Row:", int(ship_row + 1), "|| Col:", int(ship_col + 1))

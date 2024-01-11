# ----------------------------------------------------------------------------
#   Functions related to puzzle board
#       (1) Print puzzle board to the output in form of:
#           +---+---+---+---+---+---+---+---+
#           | Q |   |   |   |   | Q |   |   |
#           +---+---+---+---+---+---+---+---+
#           |   |   | Q |   |   |   |   |   |
#           +---+---+---+---+---+---+---+---+
#           |   |   |   |   |   |   |   |   |
#           +---+---+---+---+---+---+---+---+
#           |   |   |   |   |   |   |   |   |
#           +---+---+---+---+---+---+---+---+
#           |   |   |   | Q |   |   |   | Q |
#           +---+---+---+---+---+---+---+---+
#           |   | Q |   |   |   |   |   |   |
#           +---+---+---+---+---+---+---+---+
#           |   |   |   |   |   |   |   |   |
#           +---+---+---+---+---+---+---+---+
#           |   |   |   |   | Q |   | Q |   |
#           +---+---+---+---+---+---+---+---+
#       (2) Generate random boards for initial state
# ----------------------------------------------------------------------------


import random


def print_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        line += '+---+---+---+---+---+---+---+---+\n'
        for col in range(n):
            if board[col] == row:
                line += "| Q "
            else:
                line += "|   "
        line += "|"
        print(line)
    print("+---+---+---+---+---+---+---+---+\n")


def generate_random_board(board_size):
    return [random.randint(0, board_size - 1) for _ in range(board_size)]
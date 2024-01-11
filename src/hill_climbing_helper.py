# ----------------------------------------------------------------------------
#   Helper functions for hill-climbing algorithm
#       (1) Compute the heuristic of a board and return the heuristic 
#               (the number of conflicts in the board)
#       (2) Return all the neighbor boards for the current boards
# ----------------------------------------------------------------------------


def compute_heuristic(board):

    # Initialize heuristic to 0 
    h = 0

    # Check across rows and columns for conflicts
    for i in range(len(board)):
        for j in range(i + 1, len(board)):

            # Check if same number or on same diagonal
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                h += 1

    # Return number of conflicts
    return h


def get_neighbors(board):

    # Initialize list to hold neighbor boards
    neighbors = []

    # Iterate through board
    for i in range(len(board)):
        for j in range(len(board)):

            # Skip if number already in row
            if board[i] != j:

                # Copy board and swap position
                new_board = list(board)
                new_board[i] = j

                # Add modified board to neighbors
                neighbors.append(new_board)

    # Return board's neighbors        
    return neighbors
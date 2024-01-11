# ----------------------------------------------------------------------------
#   Hill-Climbing algorithm
# ----------------------------------------------------------------------------


from hill_climbing_helper import *


def steepest_ascent_hill_climbing(board):

    # Start with the initial board state
    current = board
    neighbor = None

    # Track search cost
    search_cost = 0

    while True:

        # Get neighbors' states
        neighbors = get_neighbors(current)

        search_cost += len(neighbors)

        # Compute heuristic value for current state
        current_heuristic = compute_heuristic(current)

        # Initialize next state heuristic as infinity
        next_heuristic = float('inf')

        # Evaluate neighbors
        for i in neighbors:
            heuristic = compute_heuristic(i)

            # Find neighbor with lowest heuristic
            if heuristic < next_heuristic:
                neighbor = i
                next_heuristic = heuristic

        # If stuck in local maxima, return current state 
        if next_heuristic >= current_heuristic:
            break

        # Set next state and repeat    
        current = neighbor

    return current, search_cost
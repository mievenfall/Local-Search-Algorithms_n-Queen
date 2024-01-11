# ----------------------------------------------------------------------------
#   Helper functions for genetic algorithm
#       (1) Compute the heuristic of a board and return the heuristic 
#               (the number of conflicts in the board)
#       (2) Return random generated boards
#       (3) Fitness function to to calculate fitness of an individual
#       (4) Random selection for selecting parents
#       (5) Get child from parents
#       (6) Random mutating board
# ----------------------------------------------------------------------------


import random
import numpy as np
import board

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


def initialize_population(population_size, board_size):

    # Generate random 8x8 boards in range of population_size
    return [board.generate_random_board(board_size) for _ in range(population_size)]


def fitness(board, max_heuristic):

    # Calculate the distance between max heuristic and the current heuristic
    return max_heuristic - compute_heuristic(board)


def random_selection(population, fitness_fn):

    # Calculate selection probabilities
    total_fitness = sum(fitness_fn)
    selection_probs = [i / total_fitness for i in fitness_fn]

    # Pick board based on probabilities
    return population[np.random.choice(len(population), p=selection_probs)]


def reproduce(x, y):

    # Apply crossover
    c = random.randint(0, len(x) - 1)
    return x[:c] + y[c:]


def mutate(board):

    # Randomly mutate board
    i = random.randint(0, len(board) - 1)
    board[i] = random.randint(0, len(board) - 1)
    return board
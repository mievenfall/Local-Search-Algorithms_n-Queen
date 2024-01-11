# ----------------------------------------------------------------------------
#   CS4200 -- Project 2: N-Queen (n = 8)
#
#   Solving n-Queen problems using Local search algorithms
#   There are two algorithms implemented: 
#       (1) Straight-forward steepest-ascent hill climbing;
#       (2) Genetic algorithm.
#   Input: 
#       Enter a number of instances for generating n-Queen problems
#   Output:
#       (1) With number of instances < 5:
#               Initial board and final board will be printed out
#                   - Q is Queen
#               Result will be printed out after every solved board
#       (2) With number of instances >= 5:
#               Result will be printed out after every solved board
# ----------------------------------------------------------------------------


# Import dependencies
import time
import board
from hill_climbing_algorithm import *
from genetic_algorithm import *


# Main solver function
def run(num_instances, board_size = 8, population_size = 100, generations = 100):

    # Track stats for Hill Climbing
    num_hill_climbing_success = 0
    hill_climbing_total_search_costs = 0
    hill_climbing_total_time = 0

    # Track stats for Genetic Algorithm
    num_genetic_algorithm_success = 0
    genetic_algorithm_total_search_costs = 0
    genetic_algorithm_total_time = 0

    # Loop for instances
    for _ in range(num_instances):
        
        # Initialize problem board
        initial_board = board.generate_random_board(board_size)

        # Track of number of iterations
        print('\n')
        print('{}/{}'.format((_ + 1), num_instances))

        # Print board if instances < 5
        if num_instances < 5:
            print("Initial Board:")
            board.print_board(initial_board)

        # Solve with Hill Climbing
        start_time = time.time()

        hill_climbing_final_board, hill_climbing_search_cost = steepest_ascent_hill_climbing(initial_board)

        end_time = time.time()
        hill_climbing_runtime = (end_time - start_time) * 1000

        # Accumulate stats for Hill Climbing
        hill_climbing_total_time += hill_climbing_runtime
        hill_climbing_total_search_costs += hill_climbing_search_cost

        # Check success and increment counter
        if compute_heuristic(hill_climbing_final_board) == 0:
            num_hill_climbing_success += 1


        # Solve with Genetic Algortihm
        start_time = time.time()

        genetic_algorithm_final_board, genetic_algorithm_search_cost = genetic_algorithm(population_size, board_size, generations)

        end_time = time.time()
        genetic_algorithm_runtime = (end_time - start_time) * 1000

        # Accumulate stats for Genetic Algortihm
        genetic_algorithm_total_time += genetic_algorithm_runtime
        genetic_algorithm_total_search_costs += genetic_algorithm_search_cost

        # Check success and increment counter
        if compute_heuristic(genetic_algorithm_final_board) == 0:
            num_genetic_algorithm_success += 1

        # Print board if instances < 5
        if num_instances < 5:
            print("Hill Climibing Final Board:")
            board.print_board(hill_climbing_final_board)
            print("Genetic Algorithm Final Board:")
            board.print_board(genetic_algorithm_final_board)


        # Print results
        print('Results for {}/{}'.format((_ + 1), num_instances))
        if num_instances < 5:
            print('Hill Climbing Search Cost:', hill_climbing_search_cost)
            print('Hill Climbing Runtime: {} ms'.format(hill_climbing_runtime))
            print('------------------------------------')
            print('Genetic Algorithm Search Cost:', genetic_algorithm_search_cost)
            print('Genetic Algorithm Runtime: {} ms'.format(genetic_algorithm_runtime))
            print('------------------------------------\n')
        print('Hill Climbing Success Rate: {}%'.format(num_hill_climbing_success / num_instances * 100))
        print('Hill Climbing Avg Search Cost:', hill_climbing_total_search_costs / num_instances)
        print('Hill Climbing Avg Runtime: {} ms'.format(hill_climbing_total_time / num_instances))
        print('------------------------------------')
        print('Genetic Algorithm Success Rate: {}%'.format(num_genetic_algorithm_success / num_instances * 100))
        print('Genetic Algorithm Avg Search Cost:', genetic_algorithm_total_search_costs / num_instances)
        print('Genetic Algorithm Avg Runtime: {} ms'.format(genetic_algorithm_total_time / num_instances))
        
    
# Runtime logic
def main():
    num_instances = int(input("Enter a number of instances for n-Queen problems: "))
    run(num_instances)

if __name__ == '__main__':
    main()

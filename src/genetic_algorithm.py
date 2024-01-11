# ----------------------------------------------------------------------------
#   Genetic algorithm
# ----------------------------------------------------------------------------


from genetic_algorithm_helper import *


def genetic_algorithm(population_size, board_size, generations):
    
    # Calculate max possible heuristic
    max_heuristic = (board_size * (board_size - 1)) // 2

    # Initialize population - a set of individual
    population = initialize_population(population_size, board_size)

    # A function that measures the fitness of an individial
    fitness_fn = [fitness(individual, max_heuristic) for individual in population]

    # Track search cost
    search_cost = 0

    for i in range(generations):

        # Initialize empty set of new_population
        new_population = []

        # Track search cost
        search_cost += len(population)

        # Create next generation
        for _ in range(len(population)):

            # Select parents
            x = random_selection(population, fitness_fn)
            y = random_selection(population, fitness_fn)

            # Create child  
            child = reproduce(x, y)

            # Random mutation with small random probability
            if random.random() < 0.1:
                child = mutate(child)

            new_population.append(child)

        # Update population
        population = new_population

        # Find current best individual
        best_individual = max(population, key=lambda individual: fitness(individual, max_heuristic))
        if compute_heuristic(best_individual) == 0:
            return best_individual, search_cost

    # Return best solution found
    return max(population, key=lambda individual: fitness(individual, max_heuristic)), search_cost
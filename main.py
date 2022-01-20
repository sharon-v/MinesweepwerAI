from config import *
from utils import print_elements, print_board_in_format
from generate_population import *
from scipy.special import comb
from localSearchAlgorithm import *
import geneticAlgorithm as ga

if __name__ == '__main__':
    ms_board = BEGINNER_BOARD
    num_mines = BEGINNER_MINES_NUMBER
    # key: string row+col: set(neighbors)
    # e.g. [3,4] key: 3+4
    all_uncovered_neighbors = {}
    initial_population = generate_population(ms_board, BEGINNER_POPULATION, all_uncovered_neighbors)

    population = copy.deepcopy(initial_population)

    print('generated population = {}'.format(min(shape_of_population(population))))

    num_generations = 5
    num_parents = 4

    global_optimal = len(ms_board) * len(ms_board[0])
    optimal_ga = []
    optimal_ls = []

    for generation in range(num_generations):
        # if the best solution was found.
        if len(population) == 1:
            break
        print("\n~~~~~~~~~~~~~~~~~~~~")
        print("\tGeneration {} ".format(generation))
        print("~~~~~~~~~~~~~~~~~~~~")

        # print game number and replace steps with board
        for i in range(len(population)):
            print("Game {} - Generation {}".format(i + 1, generation))
            # print("steps", population[i])  # instead, print the board
            print_board_view(ms_board, population[0])  # maybe add pboard???????????????????????????

        num_parents = min(num_parents, len(population) // 2)
        best_steps = ga.cal_fitness(population)

        parents = ga.generate_parents(ms_board, population, num_parents)

        # print all parents
        print_elements("Parents", parents)

        parents_size = len(parents)
        offsprings_size = int(comb(parents_size, 2))
        offsprings = ga.crossover(parents, offsprings_size)

        # print all offsprings
        print_elements("Babies", offsprings)

        ga.mutation(offsprings, len(ms_board), len(ms_board[0]))

        # print all offsprings
        print_elements("Mutant Babies", offsprings)

        # Create new population
        population = parents + offsprings

        ga.remove_redundant_clicks(population, all_uncovered_neighbors)

        # print('population = {}'.format(population))

        # print all Population
        print_elements("Population", population)

        print('population shape = {}'.format(shape_of_population(population)))

        optimal_ga.extend(shape_of_population(population))

        # best_steps=min(min(map(len, population)), best_steps)

        if best_steps < min(map(len, population)):
            population = initial_population
        else:
            best_steps = min(map(len, population))

        # local_search_population = generate_ls_population(population, ms_board, num_mines)
        # print('local_search_population={}'.format(local_search_population))
        # print('local_search_population shape = {}'.format(shape_of_population(local_search_population)))
        # optimal_ls.extend(shape_of_population(local_search_population))

        # best_steps=min(min(map(len, population)), best_steps)
        global_optimal = min(best_steps, global_optimal)
        # print('{}'.format(population))
        print('best result is {}'.format(best_steps))
    print("!!!!!!!!!!!!!!!!!!!")
    local_search_population = generate_ls_population(population, ms_board, num_mines)
    print('local_search_population={}'.format(local_search_population))
    print('local_search_population shape = {}'.format(shape_of_population(local_search_population)))
    optimal_ls.extend(shape_of_population(local_search_population))

    print('global optimal is {}'.format(global_optimal))
    print('optimal GA = {}'.format(min(optimal_ga)))
    print('optimal LS = {}'.format(min(optimal_ls)))

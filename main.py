import time
from scipy.special import comb

import extract_data
import geneticAlgorithm as ga
from generate_population import *
from localSearchAlgorithm import *


def run():
    # values can be changed in config
    ms_board = CURRENT_BOARD
    num_mines = CURRENT_MINE_NUMBER

    all_uncovered_neighbors = {}
    initial_population = generate_population(ms_board, BEGINNER_POPULATION, all_uncovered_neighbors)
    population = copy.deepcopy(initial_population)

    print('generated population = {}'.format(min(shape_of_population(population))))

    global_optimal = len(ms_board) * len(ms_board[0])
    optimal_ga = []
    optimal_ls = []

    ###################
    # Genetic Algorithm
    ###################

    # calc runtime of genetic
    start = time.time()
    for t in range(10000):
        True

    num_generations = 5
    num_parents = 4

    for generation in range(num_generations):
        # if the best solution was found.
        if len(population) == 1:
            break
        print("\n~~~~~~~~~~~~~~~~~~~~")
        print("\tGeneration {} ".format(generation))
        print("~~~~~~~~~~~~~~~~~~~~")

        # collect gen for csv
        extract_data.GA_GEN.append(generation)

        # print game number and replace steps with board
        for i in range(len(population)):
            print("Game {} - Generation {}".format(i + 1, generation))
            # print("steps", population[i])  # instead, print the board
            print_board_view(ms_board, population[0])

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

        # print all Population
        print_elements("Population", population)
        print('population shape = {}'.format(shape_of_population(population)))
        # collect new pop for csv
        extract_data.GA_CHROM.append(shape_of_population(population))
        optimal_ga.extend(shape_of_population(population))

        # best_steps=min(min(map(len, population)), best_steps)
        if best_steps < min(map(len, population)):
            population = initial_population
        else:
            best_steps = min(map(len, population))

        # best_steps=min(min(map(len, population)), best_steps)
        global_optimal = min(best_steps, global_optimal)

        # print('{}'.format(population))
        print('best result is {}'.format(best_steps))

    # end runtime calc
    end = time.time()

    ###################
    # Local Search
    ###################

    # calc runtime of LS
    start1 = time.time()
    for t in range(10000):
        True

    population_ls = copy.deepcopy(initial_population)
    extract_data.LS_POP.append(population_ls)
    local_search_population = generate_ls_population(population_ls, ms_board, num_mines)
    print('local_search_population={}'.format(local_search_population))
    print('local_search_population shape = {}'.format(shape_of_population(local_search_population)))
    optimal_ls.extend(shape_of_population(local_search_population))

    # end runtime calc
    end1 = time.time()

    # print('global optimal GA is {}'.format(global_optimal))
    print('optimal GA = {}'.format(min(optimal_ga)))
    print('optimal LS = {}'.format(min(optimal_ls)))

    print("Genetic RunTime: ", end - start)
    print("LocalSearch RunTime: ", end1 - start1)

    # collect runtime and opt for csv
    extract_data.GA_OPT.append([min(optimal_ga)])
    extract_data.LS_OPT.append([min(optimal_ls)])
    extract_data.GA_RTIME.append([end - start])
    extract_data.LS_RTIME.append([end1 - start1])


if __name__ == '__main__':
    num_of_runs = 1
    for n in range(num_of_runs):
        run()
        extract_data.f()

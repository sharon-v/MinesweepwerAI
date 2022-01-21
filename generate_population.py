import random
import utils

# Author: Barry, modified by happygirlzt

"""
FUNCTION uncover_neighbors
ARGUMENTS: pBoard, mBoard, unOpenedFeasibleList, row, col

pBoard => playing board
record opened and unopened cells in board (0 for unopened, 1 for opened)

mBoard => map board (i.e BEGINNER_BOARD)
contains value of each cell, -1 means 'mine'

unOpenedFeasibleList => a list containing non mines clicks available for next clicks

row => the clicked row, col => the clicked column

res is for accumulating how many cells could be uncovered => fitness
"""


def uncover_neighbors(pBoard, mBoard, unOpenedFeasibleList, row, col, uncovered_neighbors):
    if pBoard[row][col] == 1:
        return

    uncovered_neighbors.add(str(row) + '+' + str(col))

    cellNumber = mBoard[row][col]
    pBoard[row][col] = 1
    unOpenedFeasibleList.remove([row, col])

    if cellNumber == 0:
        if row > 0:
            uncover_neighbors(pBoard, mBoard, unOpenedFeasibleList, row - 1, col, uncovered_neighbors)
        if row < len(pBoard) - 1:
            uncover_neighbors(pBoard, mBoard, unOpenedFeasibleList, row + 1, col, uncovered_neighbors)
        if col > 0:
            uncover_neighbors(pBoard, mBoard, unOpenedFeasibleList, row, col - 1, uncovered_neighbors)
        if col < len(pBoard[0]) - 1:
            uncover_neighbors(pBoard, mBoard, unOpenedFeasibleList, row, col + 1, uncovered_neighbors)


# FUNCTION generate_population
# ARGUMENTS: mBoard, populationSize
# fitness is calculated as least moves in the solutions
def generate_population(mBoard, populationSize, all_uncovered_neighbors):
    # Generate unOpenedFeasibleList
    unOpenedFeasibleList = utils.generate_unopened_list(mBoard)

    # Copy the default unOpenedFeasibleList
    defaultUnOpened = unOpenedFeasibleList.copy()

    count = 1
    population = []
    boardRows = len(mBoard)
    boardCols = len(mBoard[0])

    while count <= populationSize:
        # initialize chromosome, unOpenedFeasibleList, and pBoard
        chromosome = []

        unOpenedFeasibleList = defaultUnOpened.copy()
        pBoard = []
        rowsCount = 0
        while rowsCount < boardRows:
            pBoard.append([0] * boardCols)
            rowsCount += 1
        # until here we initialized the pBoard to 0

        uncovered_neighbors = set()
        # chromosome created if no more non-mine cell available to be clicked
        while len(unOpenedFeasibleList) > 0:
            # generate genes
            gen = random.choice(unOpenedFeasibleList)
            chromosome.append(gen)

            if mBoard[gen[0]][gen[1]] != 0:
                pBoard[gen[0]][gen[1]] = 1
                unOpenedFeasibleList.remove(gen)
            else:
                uncover_neighbors(pBoard, mBoard, unOpenedFeasibleList, gen[0], gen[1], uncovered_neighbors)

        print()
        if chromosome not in population:
            print("chromosome-", count, " = ", chromosome)
            print("amount of chromosomes: ", len(chromosome))
            population.append(chromosome)

            first_click = chromosome[0]
            click_key = str(first_click[0]) + '+' + str(first_click[1])

            all_uncovered_neighbors[click_key] = uncovered_neighbors
            #
            # chromosome_fitness = copy.deepcopy(chromosome)
            # chromosome_fitness.insert(0, cells_opened)
            # pop_fitness.append((cells_opened, chromosome))
            # pop_fitness.append((len(chromosome), chromosome))
            #
            count = count + 1

    return population

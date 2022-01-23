import extract_data
from config import *
from utils import *
import copy


def find_new_click(board):
    res_i = 0
    res_j = 0
    # print("find new click : ")
    # print_board_in_format(board)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                # print("the click in 'find new' func: ", [i, j])
                return i, j
            else:
                if (board[i][j] != -2) & (board[i][j] != -1):
                    res_i = i
                    res_j = j
    # print("the click in 'find new' func: ", [i, j])
    return res_i, res_j


def local_search(clicks, kept_percent, board, mines_number):
    kept_clicks = int(len(clicks) * kept_percent)
    temp_board = copy.deepcopy(board)
    clicks_return = clicks[:kept_clicks]
    print("Click ", clicks)
    print("clicks_return ", clicks_return)
    number_of_opened_cells = len(board) * len(board[0]) - mines_number
    y = 0
    for i in range(kept_clicks):
        if temp_board[clicks[i][0]][clicks[i][1]] != 0 & temp_board[clicks[i][0]][clicks[i][1]] != -2:
            temp_board[clicks[i][0]][clicks[i][1]] = -2  # opened
            number_of_opened_cells = number_of_opened_cells - 1

        if temp_board[clicks[i][0]][clicks[i][1]] == 0:
            # open multiple cells
            temp_board, number_of_opened_cells = open_cell_zero(clicks[i][0], clicks[i][1], temp_board,
                                                                number_of_opened_cells)

            # print_board_view(temp_board, clicks_return)
        # print("Local Search Game Num ", i)
        # print_board_view(board, clicks_return)

    while number_of_opened_cells > 0:
        new_i, new_j = find_new_click(temp_board)
        clicks_return.append([new_i, new_j])
        if temp_board[new_i][new_j] != 0 & temp_board[new_i][new_j] != -2:
            temp_board[new_i][new_j] = -2  # opened
            number_of_opened_cells = number_of_opened_cells - 1
            # print_board_view(temp_board, clicks_return)
        if temp_board[new_i][new_j] == 0:
            # open multiple cells
            temp_board, number_of_opened_cells = open_cell_zero(new_i, new_j, temp_board,
                                                                number_of_opened_cells)
            # print_board_view(temp_board, clicks_return)
    # print("Local Search Game Num ")
    # print_board_in_format(temp_board)
    # print("blalalal")
    # print_board_view(board, clicks_return)
    # print_board_view(board, clicks_return)
    return clicks_return, temp_board


def generate_ls_population(population, ms_board, num_mines):
    ls_population = []
    print("local search population", population)
    popforcsv = []
    temp_board = []
    y = 0
    for population_i in population:
        steps = len(population_i)
        best_ls_result = population_i
        print("population  :", population_i)
        keptforcsv = []
        for i in LOCAL_SEARCH_KEPT_PERCENT:
            print("Local Search Game  ", i)
            ls_result, temp_board = local_search(population_i, i, ms_board, num_mines)
            # collect for csv
            keptforcsv.append(len(ls_result))
            print("keptfocsv:", keptforcsv)
            print("ls_result:  ", ls_result)

            # print_board_view(ms_board, ls_result)
            if len(ls_result) < steps:
                steps = len(ls_result)
                best_ls_result = ls_result
        ls_population.append(best_ls_result)
        y += 1
        print("Current kept percent: ", y)
        y = 0
        # collect for csv
        popforcsv.append(keptforcsv)
    extract_data.LS_POP.append(popforcsv)
    return ls_population

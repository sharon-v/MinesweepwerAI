import copy


# opens all cells bordering the cell if a 0 cell is opened
def open_cell_zero(cell_position_x, cell_position_y, board, number_of_opened_cells):
    temp_board = copy.deepcopy(board)
    if temp_board[cell_position_x][cell_position_y] != 0:
        temp_board[cell_position_x][cell_position_y] = -2  # opened
        number_of_opened_cells = number_of_opened_cells - 1
        return temp_board, number_of_opened_cells
    if temp_board[cell_position_x][cell_position_y] == 0:
        temp_board[cell_position_x][cell_position_y] = -2  # opened
        number_of_opened_cells = number_of_opened_cells - 1  # opened
        # Left
        if (cell_position_y - 1 >= 0) & (temp_board[cell_position_x][cell_position_y - 1] != -2):  # not opened yet
            temp_board, number_of_opened_cells = open_cell_zero(cell_position_x, cell_position_y - 1, temp_board,
                                                                number_of_opened_cells)
        # Right
        if cell_position_y + 1 < len(temp_board[0]):
            if temp_board[cell_position_x][cell_position_y + 1] != -2:  # not opened yet
                temp_board, number_of_opened_cells = open_cell_zero(cell_position_x, cell_position_y + 1,
                                                                    temp_board, number_of_opened_cells)
        # Down
        if cell_position_x + 1 < len(temp_board):
            if temp_board[cell_position_x + 1][cell_position_y] != -2:  # not opened yet
                temp_board, number_of_opened_cells = open_cell_zero(cell_position_x + 1, cell_position_y,
                                                                    temp_board, number_of_opened_cells)
        # Up
        if (cell_position_x - 1 >= 0) & (temp_board[cell_position_x - 1][cell_position_y] != -2):  # not opened yet
            temp_board, number_of_opened_cells = open_cell_zero(cell_position_x - 1, cell_position_y, temp_board,
                                                                number_of_opened_cells)
        # Up Left
        if (cell_position_y - 1 >= 0) & (cell_position_x - 1 >= 0) & (
                temp_board[cell_position_x - 1][cell_position_y - 1] != -2):  # not opened yet
            temp_board, number_of_opened_cells = open_cell_zero(cell_position_x - 1, cell_position_y - 1,
                                                                temp_board, number_of_opened_cells)

        # Up Right
        if (cell_position_y + 1 < len(temp_board[0])) & (cell_position_x - 1 >= 0):
            if temp_board[cell_position_x - 1][cell_position_y + 1] != -2:  # not opened yet
                temp_board, number_of_opened_cells = open_cell_zero(cell_position_x - 1, cell_position_y + 1,
                                                                    temp_board, number_of_opened_cells)
        # Down Left
        if (cell_position_y - 1 >= 0) & (cell_position_x + 1 < len(temp_board)):
            if temp_board[cell_position_x + 1][cell_position_y - 1] != -2:  # not opened yet
                temp_board, number_of_opened_cells = open_cell_zero(cell_position_x + 1, cell_position_y - 1,
                                                                    temp_board, number_of_opened_cells)

        # Down Right
        if (cell_position_y + 1 < len(temp_board[0])) & (cell_position_x + 1 < len(temp_board)):
            if temp_board[cell_position_x + 1][cell_position_y + 1] != -2:  # not opened yet
                temp_board, number_of_opened_cells = open_cell_zero(cell_position_x + 1, cell_position_y + 1,
                                                                    temp_board, number_of_opened_cells)
    return temp_board, number_of_opened_cells


def is_solution(clicks, board, mines_number):
    """
    Check if 'clicks' is a solution
    :param clicks: [(7, 7), (0, 0), (0,7), (7, 0), (4,6), (7, 5)]
    :param board: BEGINNER_BOARD
    :param mines_number: BEGINNER_MINES_NUMBER
    :return: True if this is a solution, otherwise False
    """
    temp_board = copy.deepcopy(board)
    number_of_opened_cells = len(board) * len(board[0]) - mines_number
    for click in clicks:
        if number_of_opened_cells == 0:
            return True
        if temp_board[click[0]][click[1]] == -1:  # mine
            return False
        if temp_board[click[0]][click[1]] != 0 & temp_board[click[0]][click[1]] != -2:
            temp_board[click[0]][click[1]] = -2  # opened
            number_of_opened_cells = number_of_opened_cells - 1
        if temp_board[click[0]][click[1]] == 0:
            # open multiple cells
            temp_board, number_of_opened_cells = open_cell_zero(click[0], click[1], temp_board, number_of_opened_cells)
    if number_of_opened_cells == 0:
        return True
    return False


def shape_of_population(population):
    res = []
    for i in population:
        res.append(len(i))
    return res


#  ~~~~~~~~~~~~~~~~~~~~~~~ print functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# additional func to print list elements
def print_elements(parameter_name, elements):
    num = 1
    print("** " + parameter_name + " **")
    for e in elements:
        print(" {0} {1} = {2}".format(parameter_name, num, e))
        num += 1
    print()


# board printing in a game format
def print_board_in_format(board):
    for x in board:
        for y in x:
            print(" {} ".format(y), end="")
        print()
    print()


def print_current_board_for_view(pBoard, mBoard):
    # create empty board
    board_to_print = []
    for i in range(len(pBoard), 0, -1):
        board_to_print.append([0] * len(pBoard[0]))

    count_covered_cells = 0
    for row in range(len(pBoard)):
        for col in range(len(pBoard[0])):
            if pBoard[row][col] == 1:
                board_to_print[row][col] = mBoard[row][col]
            else:
                count_covered_cells += 1

    print("covered cells: ", count_covered_cells)
    print_board_in_format(board_to_print)


#  prints the board for the players view
def print_board_view(msBoard, moves):   # maybe add pboard???????????????????
    # create empty board
    board_to_print = []
    unOpenedFeasibleList = generate_unopened_list(msBoard)
    uncovered_neighbor = []
    # fill board as covered
    for i in range(len(msBoard), 0, -1):
        board_to_print.append(['*'] * len(msBoard[0]))

    # uncover cells and re-print board
    for m in moves:
        x = m[0]
        y = m[1]
        cur_move = msBoard[x][y]

        # if cur_move == -1:
        #     board_to_print[x][y] = '!'
        # elif cur_move == 0:
        #     pass  # need to open all cells until the border is not 0's
        # elif cur_move != 0:
        #     board_to_print[x][y] = msBoard[x][y]
        uncover_neighbors_modified(board_to_print, msBoard, unOpenedFeasibleList, x, y)
        # print the board
        print_board_in_format(board_to_print)


def generate_unopened_list(board):
    unOpenedFeasibleList = []
    row = 0
    while row < len(board):
        col = 0
        while col < len(board[0]):
            if board[row][col] != -1:
                gen = [row, col]
                unOpenedFeasibleList.append(gen)
            col = col + 1
        row = row + 1
    return unOpenedFeasibleList


def uncover_neighbors_modified(viewBoard, msBoard, unOpenedFeasibleList, x, y):

    if viewBoard[x][y] != '*':
        return

    cellNumber = msBoard[x][y]
    # viewBoard[row][col] = 1
    if msBoard[x][y] == -1:
        viewBoard[x][y] = '!'
    elif msBoard[x][y] == 0:
        # need to open all cells until the border is not 0's
        if cellNumber == 0:
            if x > 0:
                uncover_neighbors_modified(viewBoard, msBoard, unOpenedFeasibleList, x - 1, y)
            if x < len(viewBoard) - 1:
                uncover_neighbors_modified(viewBoard, msBoard, unOpenedFeasibleList, x + 1, y)
            if y > 0:
                uncover_neighbors_modified(viewBoard, msBoard, unOpenedFeasibleList, x, y - 1)
            if y < len(viewBoard[0]) - 1:
                uncover_neighbors_modified(viewBoard, msBoard, unOpenedFeasibleList, x, y + 1)
    elif msBoard[x][y] != 0:
        viewBoard[x][y] = msBoard[x][y]

    unOpenedFeasibleList.remove([x, y])



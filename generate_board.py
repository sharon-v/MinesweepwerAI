import random

rows = 8
cols = 8
num_mines = 10

board = [[0 for i in range(0, rows)] for j in range(0, cols)]

board_coordinates = [(x, y) for x in range(0, cols) for y in range(0, rows)]

mine_coordinates = random.sample(board_coordinates, num_mines)

for mine in mine_coordinates:
    x, y = mine
    board[x][y] = -1
    neighbors = [(x - 1, y), (x - 1, y + 1), (x, y - 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1), (x, y + 1),
                 (x - 1, y - 1)]
    for n in neighbors:
        if 0 <= n[0] <= cols - 1 and 0 <= n[1] <= rows - 1 and n not in mine_coordinates:
            board[n[0]][n[1]] += 1


# ###### testing ######:
def get_mine_neighbors(x, y):
    mines = []
    neighbors = [(x - 1, y), (x - 1, y + 1), (x, y - 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1), (x, y + 1),
                 (x - 1, y - 1)]
    for n in neighbors:
        if 0 <= n[0] <= cols - 1 and 0 <= n[1] <= rows - 1:
            if board[n[0]][n[1]] == 9:
                mines.append(n)
    return mines


for r in board:
    print(r)

for r in mine_coordinates:
    print(r)

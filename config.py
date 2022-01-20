# -1 means 'mine'
# 8 * 8
BEGINNER_BOARD = [[0, 1, -1, 1, 0, 0, 0, 0],
                  [2, 3, 2, 1, 0, 0, 1, 1],
                  [-1, -1, 1, 0, 0, 1, 3, -1],
                  [2, 3, 2, 1, 0, 1, -1, -1],
                  [0, 2, -1, 2, 0, 1, 3, -1],
                  [0, 2, -1, 2, 1, 1, 2, 1],
                  [0, 1, 1, 1, 1, -1, 1, 0],
                  [0, 0, 0, 0, 1, 1, 1, 0]]
BEGINNER_MINES_NUMBER = 10

MEDIUM_BOARD = [[0, 0, 0, 0, 0, 1, -1, 2, 1, 0, 1, 1, 2, 1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0, 1, 3, -1, 2, 0, 1, -1, 3, -1, 2, 0, 0, 0],
                [-1, 1, 0, 1, 2, 2, 4, -1, 4, 1, 1, 1, 3, -1, 2, 0, 0, 0],
                [1, 1, 1, 2, -1, -1, 5, -1, -1, 2, 1, 0, 1, 1, 2, 2, 2, 1],
                [0, 0, 1, -1, 4, -1, 4, -1, 4, -1, 1, 1, 1, 1, 1, -1, -1, 1],
                [0, 0, 1, 1, 2, 1, 2, 2, 3, 2, 2, 2, -1, 1, 1, 2, 2, 1],
                [1, 1, 1, 0, 0, 1, 1, 2, -1, 2, 2, -1, 2, 1, 0, 0, 1, 1],
                [1, -1, 2, 1, 0, 1, -1, 3, 2, 3, -1, 2, 1, 0, 0, 0, 1, -1],
                [2, 3, -1, 1, 0, 1, 1, 3, -1, 3, 1, 1, 0, 0, 0, 0, 1, 1],
                [2, -1, 3, 1, 0, 0, 0, 3, -1, 4, 1, 0, 0, 0, 0, 0, 0, 0],
                [3, -1, 3, 0, 0, 0, 0, 3, -1, -1, 1, 0, 1, 1, 1, 0, 0, 0],
                [2, -1, 3, 1, 0, 0, 0, 2, -1, 4, 2, 0, 1, -1, 1, 0, 0, 0],
                [2, 3, -1, 1, 0, 0, 0, 2, 3, -1, 2, 1, 1, 2, 2, 1, 0, 0],
                [1, -1, 2, 1, 0, 0, 0, 1, -1, 3, -1, 1, 0, 1, -1, 1, 0, 0]]
MEDIUM_MINES_NUMBER = 40

HARD_BOARD = [[0, 0, 0, 0, 0, 1, -1, 1, 1, -1, -1, 3, -1, 1, 0, 1, -1, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 3, -1, 4, 3, 2, 2, 2, 1, 0, 0, 1, 1, 1, 0],
              [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 2, -1, -1, 3, -1, 4, 2, 1, 0, 1, -1, 1, 0],
              [1, -1, 3, 3, -1, 1, 0, 2, -1, 3, 1, 2, 2, 2, 4, -1, -1, -1, 2, 1, 3, 2, 3, 1],
              [2, 3, -1, -1, 2, 1, 0, 3, -1, 4, -1, 2, 1, 1, 2, -1, -1, 3, 2, -1, 3, -1, 3, -1],
              [3, -1, 4, 2, 1, 0, 1, 4, -1, 4, 1, 2, -1, 1, 1, 2, 2, 1, 2, 2, 4, -1, 4, 2],
              [-1, -1, 4, 1, 1, 1, 2, -1, -1, 3, 1, 2, 2, 2, 2, 1, 2, 1, 3, -1, 3, 1, 2, -1],
              [-1, -1, -1, 1, 1, -1, 2, 2, 3, 3, -1, 1, 1, -1, 2, -1, 2, -1, 4, -1, 2, 0, 1, 1],
              [3, -1, 3, 2, 3, 3, 2, 0, 2, -1, 3, 1, 1, 1, 2, 1, 2, 2, -1, 2, 1, 0, 0, 0],
              [1, 1, 1, 1, -1, -1, 1, 0, 2, -1, 3, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
              [0, 0, 0, 1, 2, 2, 1, 0, 1, 1, 3, -1, 2, 0, 0, 0, 1, 1, 2, 1, 2, 2, -1, 1],
              [0, 1, 1, 2, 1, 1, 0, 0, 0, 0, 2, -1, 3, 1, 1, 0, 1, -1, 3, -1, 2, -1, 3, 2],
              [1, 2, -1, 3, -1, 3, 1, 1, 0, 0, 1, 2, 3, -1, 1, 0, 1, 2, -1, 2, 2, 1, 2, -1],
              [-1, 3, 2, 4, -1, 3, -1, 2, 2, 1, 2, 2, -1, 3, 3, 1, 2, 2, 2, 1, 0, 0, 2, 2],
              [2, 3, -1, 3, 2, 3, 3, -1, 2, -1, 2, -1, 3, -1, 4, -1, 3, -1, 2, 1, 0, 0, 2, -1],
              [1, -1, 3, -1, 2, 2, -1, 2, 2, 1, 2, 1, 3, 4, -1, -1, 4, 3, -1, 2, 1, 1, 2, -1],
              [1, 1, 2, 1, 2, -1, 3, 3, 1, 1, 0, 0, 1, -1, -1, 4, 4, -1, 4, 3, -1, 3, 3, 2],
              [0, 0, 1, 1, 2, 2, -1, 2, -1, 1, 0, 0, 1, 2, 3, -1, 3, -1, -1, 3, 3, -1, -1, 1],
              [0, 0, 2, -1, 2, 2, 2, 3, 1, 2, 1, 1, 1, 1, 2, 1, 2, 2, 3, 3, -1, 3, 2, 1],
              [0, 0, 2, -1, 2, 1, -1, 1, 0, 1, -1, 1, 1, -1, 1, 0, 0, 0, 1, -1, 2, 1, 0, 0]]
HARD_MINES_NUMBER = 99

LOCAL_SEARCH_KEPT_PERCENT = [0.75, 0.5, 0.25]
# LOCAL_SEARCH_KEPT_PERCENT = [0.25, 0.12, 0.05]
BEGINNER_POPULATION = 10

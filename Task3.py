grid1=[[1,0,3,4,5,6],
       [4,5,6,1,0,3],
       [0,3,4,5,6,1],
       [5,6,1,0,3,4],
       [3,4,5,6,1,0],
       [6,1,0,3,4,5]]
# 测试用数独，随便写的

import sys
import time

grids = [(grid1, 3, 3)]
#def solve(grid, n_rows, n_cols):
def check_section(section, n):
    if len(set(section)) == len(section) and sum(section) == sum([i for i in range(n + 1)]):
        return True
    return False


def get_squares(grid, n_rows, n_cols):
    squares = []
    for i in range(n_cols):
        rows = (i * n_rows, (i + 1) * n_rows)
        for j in range(n_rows):
            cols = (j * n_cols, (j + 1) * n_cols)
            square = []
            for k in range(rows[0], rows[1]):
                line = grid[k][cols[0]:cols[1]]
                square += line
            squares.append(square)

    return squares


def check_solution(grid, n_rows, n_cols):
    '''
    This function is used to check whether a sudoku board has been correctly solved

    args: grid - representation of a sudoku board as a nested list.
    returns: True (correct solution) or False (incorrect solution)
    '''
    n = n_rows * n_cols

    for r in grid:
        if not check_section(r, n):
            return False

    for i in range(n):
        column = []
        for j in grid:
            column.append(j[i])

        if not check_section(column, n):
            return False

    squares = get_squares(grid, n_rows, n_cols)
    for square in squares:
        if not check_section(square, n):
            return False

    return True





def start(grid):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 0:
                return x, y
    return False, False


def next(grid, x, y):
    n=len(grid)
    for next_y in range(y + 1, n):
        if grid[x][next_y] == 0:
            return x, next_y
    for next_x in range(x + 1, n):
        for next_y in range(0, n):
            if grid[next_x][next_y] == 0:
                return next_x, next_y
    return -1, -1


def value(grid, x, y, n_rows, n_cols):
    n = n_rows*n_cols
    i, j = x // n_cols, y // n_rows
    M = [grid[i * n_cols + r][j * n_rows + c] for r in range(n_cols) for c in range(n_rows)]
    v = set([x for x in range(1, n + 1)]) - set(M) - set(grid[x]) - set(list(zip(*grid))[y])

    return list(v)


def solution(grid, x, y, n_rows, n_cols, explain):
    for grid[x][y] in value(grid, x, y, n_rows, n_cols):
        if explain is True:
            print("Place %s into grid cell (%s, %s)" % (grid[x][y], x, y))
        next_x, next_y = next(grid, x, y)
        if next_y == -1:
            return grid
        elif solution(grid, next_x, next_y, n_rows, n_cols, explain):
            return grid
        else:
            grid[x][y] = 0


def main(arguments):
    explain = False
    if '--explain' in arguments:
        explain = True
    points = 0
    print("Running test script for coursework 1")
    print("====================================")

    for (i, (grid, n_rows, n_cols)) in enumerate(grids):
        print("Solving grid: %d" % (i + 1))  # show the order of grids
        start_time = time.time()
        x, y = start(grid)
        Fsolution = solution(grid, x, y, n_rows, n_cols, explain)
        elapsed_time = time.time() - start_time
        print("Solved in: %f seconds" % elapsed_time)
        print(Fsolution)
        if check_solution(Fsolution, n_rows, n_cols):
            print("grid %d correct" % (i + 1))  # modify it could fit 3 by 3 soduku
            points = points + 10
        else:
            print("grid %d incorrect" % (i + 1))  # modify it could fit 3 by 3 soduku

    print("====================================")
    print("Test script complete, Total points: %d" % points)


if __name__ == "__main__":
    # runs main with the arguments after the initial call (flags) passed
    args = sys.argv[1:]
    print(args)
    main(args)
       
      

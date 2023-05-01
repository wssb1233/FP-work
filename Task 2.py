# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 06:13:37 2023

@author: 48601
"""

import argparse

grid1 = [[0,0,3,4,5,6],
         [4,5,6,1,0,3],
         [0,3,4,5,6,1],
         [5,6,1,0,3,4],
         [3,4,5,6,1,0],
         [6,1,0,3,4,5]]
# 测试用数独，随便写的

def solve(grid, n_rows, n_cols, explain=False, hint=0):
    explanation = []
    hints = [0]
    result = sudoku(grid, explanation, hints, n_rows, n_cols, hint, explain)
    return result

def start(grid):
    n = len(grid)
    for x in range(n):
        for y in range(n):
            if grid[x][y] == 0:
                return x, y
    return False, False


def next(grid, x, y):
    n = len(grid)
    for next_y in range(y + 1, n):
        if grid[x][next_y] == 0:
            return x, next_y
    for next_x in range(x + 1, n):
        for next_y in range(0, n):
            if grid[next_x][next_y] == 0:
                return next_x, next_y
    return -1, -1


def value(grid, x, y, n_rows, n_cols):
    n = len(grid)
    i, j = x // n_cols, y // n_rows
    M = [grid[i * n_cols + r][j * n_rows + c] for r in range(n_cols) for c in range(n_rows)]
    v = set([x for x in range(1, n+1)]) - set(M) - set(grid[x]) - set(list(zip(*grid))[y])

    return list(v)

def jie(grid, x, y, explanation, hints, n_rows, n_cols, hint, explain):
    if hints[0] == hint:
        return True

    for grid[x][y] in value(grid, x, y, n_rows, n_cols):
        if explain:
            explanation.append(f"Put {grid[x][y]} in location ({x}, {y})")
        hints[0] += 1

        next_x, next_y = next(grid, x, y)
        if next_y == -1:
            return True
        elif jie(grid, next_x, next_y, explanation, hints, n_rows, n_cols, hint, explain):
            return True
        else:
            if explain:
                explanation.append(f"Undo {grid[x][y]} from location ({x}, {y})")
            grid[x][y] = 0
            hints[0] -= 1


def sudoku(grid, explanation, hints, n_rows, n_cols, hint, explain):
    x, y = start(grid)
    jie(grid, x, y, explanation, hints, n_rows, n_cols, hint, explain)
    return grid, explanation

def read_grid_from_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        grid = [[int(num) for num in line.strip().split(',')] for line in lines]
    return grid

def write_grid_to_file(grid, output_file):
    with open(output_file, 'w') as file:
        for row in grid:
            file.write(' '.join(str(num) for num in row) + '\n')

def determine_grid_size(grid):
    n = len(grid)
    if n == 4:  # For 2x2 grid
        n_rows = 2
        n_cols = 2
    elif n == 6:  # For 3x2 grid
        n_rows = 3
        n_cols = 2
    elif n == 9:  # For 3x3 grid
        n_rows = 3
        n_cols = 3
    else:
        raise ValueError("Unsupported grid size")
    return n_rows, n_cols


def main():
    parser = argparse.ArgumentParser(description="Solver")
    parser.add_argument("--explain", action="store_true", help="Provide a set of instructions for solving the puzzle")
    parser.add_argument("--file", nargs=2, metavar=("INPUT", "OUTPUT"), help="reads a grid from a file and saves the solution to another file")
    parser.add_argument("--hint", type=int, metavar="N", help="rather than giving the full solution, instead returns a grid with N values filled in")
    parser.add_argument("--profile", action="store_true", help="measures the performance of your solvers for grids of different size and difficulties")

    args = parser.parse_args()

    if args.file:
        input_file, output_file = args.file
        grid = read_grid_from_file(input_file)
        output = True
    else:
        grid = grid1
        output = False

    n_rows, n_cols = determine_grid_size(grid)

    if output:
        solved_grid, explanation = solve(grid, n_rows, n_cols, args.explain, args.hint)
        write_grid_to_file(solved_grid, output_file)

        if args.explain:
            print('explain:')
            for each_step in explanation:
                print(each_step)
            with open(output_file, 'a') as file:
                file.write('\n\n\nExplanation:\n\n\n')
                for each_step in explanation:
                    file.write(each_step + '\n')


    else:
        solved_grid, explanation = solve(grid, n_rows, n_cols, args.explain, args.hint)
        print(solved_grid)
        if args.explain:
            print('explain:')

            for each_step in explanation:
                print(each_step)




if __name__ == "__main__":
    main()
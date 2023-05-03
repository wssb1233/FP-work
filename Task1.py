import argparse
import time
import copy
import matplotlib.pyplot as plt
import numpy as np


easy1 = [
    [9, 0, 6, 0, 0, 1, 0, 4, 0],
    [7, 0, 1, 2, 9, 0, 0, 6, 0],
    [4, 0, 2, 8, 0, 6, 3, 0, 0],
    [0, 0, 0, 0, 2, 0, 9, 8, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 9, 4, 0, 8, 0, 0, 0, 0],
    [0, 0, 3, 7, 0, 8, 4, 0, 9],
    [0, 4, 0, 0, 1, 3, 7, 0, 6],
    [0, 6, 0, 9, 0, 0, 1, 0, 8]]
easy2 = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]]

easy3 = [
    [0, 3, 0, 4, 0, 0],
    [0, 0, 5, 6, 0, 3],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 0, 3, 0, 5],
    [0, 6, 4, 0, 3, 1],
    [0, 0, 1, 0, 4, 6]]

med1 = [
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 0, 1],
    [3, 6, 9, 0, 8, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 6, 8, 0, 0],
    [0, 0, 0, 1, 3, 0, 0, 0, 9],
    [4, 0, 5, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 6, 0, 0, 7, 0, 0, 0],
    [1, 0, 0, 3, 4, 0, 0, 0, 0]]
med2 = [
    [8, 0, 9, 0, 2, 0, 3, 0, 0],
    [0, 3, 7, 0, 6, 0, 5, 0, 0],
    [0, 0, 0, 4, 0, 9, 7, 0, 0],
    [0, 0, 2, 9, 0, 1, 0, 6, 0],
    [1, 0, 0, 3, 0, 6, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 3],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [5, 0, 0, 0, 0, 0, 0, 1, 4],
    [0, 0, 0, 2, 8, 4, 6, 0, 5]]
hard1 = [
    [0, 2, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 6, 0, 4, 0, 0, 0, 0],
    [5, 8, 0, 0, 9, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 3, 0, 0, 4],
    [4, 1, 0, 0, 8, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 5],
    [2, 0, 0, 0, 1, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 1, 0, 0, 8, 0, 5, 7]]

grids = [easy1, easy2, easy3, med1, med2, hard1]

def check_solution(grid, n_rows, n_cols):
    '''
    This function is used to check whether a sudoku board has been correctly solved

    args: grid - representation of a sudoku board as a nested list.
    returns: True (correct solution) or False (incorrect solution)
    '''
    n = n_rows * n_cols

    for row in grid:
        if not check_section(row, n):
            print('A')
            return False

    for i in range(n_rows*n_cols):
        column = []
        for row in grid:
            column.append(row[i])

        if not check_section(column, n):
            print('B')
            return False

    squares = get_squares(grid, n_rows, n_cols)
    for square in squares:
        if not check_section(square, n):
            print('C')
            return False

    return True

def check_section(section, n):
    if len(set(section)) == len(section) and sum(section) == sum([i for i in range(n + 1)]):
        return True
    return False


def get_squares(grid, n_rows, n_cols):
    squares = []
    for i in range(n_rows):
        rows = (i * n_cols, (i + 1) * n_cols)
        for j in range(n_cols):
            cols = (j * n_rows, (j + 1) * n_rows)
            square = []
            for k in range(rows[0], rows[1]):
                line = grid[k][cols[0]:cols[1]]
                square += line
            squares.append(square)

    return squares

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

def recursive_solve_task_1(grid, x, y, explanation, hints, n_rows, n_cols, hint, explain):
    if hints[0] == hint:
        return True

    for grid[x][y] in value(grid, x, y, n_rows, n_cols):
        if explain:
            explanation.append(f"Put {grid[x][y]} in location ({x}, {y})")
        hints[0] += 1

        next_x, next_y = next(grid, x, y)
        if next_y == -1:
            return True
        elif recursive_solve_task_1(grid, next_x, next_y, explanation, hints, n_rows, n_cols, hint, explain):
            return True
        else:
            if explain:
                explanation.append(f"Undo {grid[x][y]} from location ({x}, {y})")
            grid[x][y] = 0
            hints[0] -= 1


def sudoku(grid, explanation, hints, n_rows, n_cols, hint, explain):
    x, y = start(grid)
    recursive_solve_task_1(grid, x, y, explanation, hints, n_rows, n_cols, hint, explain)
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

def difficulty(grid, n_rows, n_cols):
    number = 0
    for i in range(len(grid)):
        for j in range (len(grid[i])):
            if grid[i][j] == 0:
                number +=1
    ratio = number/(n_rows*n_cols)**2
    return ratio



def main():
    parser = argparse.ArgumentParser(description="Solver")
    parser.add_argument("--explain", action="store_true", help="Provide a set of instructions for solving the puzzle")
    parser.add_argument("--file", nargs=2, metavar=("INPUT", "OUTPUT"), help="reads a grid from a file and saves the solution to another file")
    parser.add_argument("--hint", type=int, metavar="N", help="rather than giving the full solution, instead returns a grid with N values filled in")
    parser.add_argument("--profile", action="store_true", help="measures the performance of your solvers for grids of different size and difficulties")

    args = parser.parse_args()

    Ttime = []
    difficulties = []
    average_time = []

    if args.file:
        input_file, output_file = args.file
        grid = read_grid_from_file(input_file)
        n_rows, n_cols = determine_grid_size(grid)
        output = True
    else:
        if not args.profile:
            points = 0
            for i in range(len(grids)):
                grid = grids[i]
                output = False

                n_rows, n_cols = determine_grid_size(grid)
                start_time = time.time()
                solved_grid, explanation = solve(grid, n_rows, n_cols, args.explain, args.hint)
                elapsed_time = time.time() - start_time
                print(f"Solved grid{i + 1}:\n", solved_grid)
                print("Solved in %f seconds" % elapsed_time)
                if check_solution(solved_grid, n_rows, n_cols):
                    print("grid %d correct" % (i + 1))  # modify it could fit 3 by 3 soduku
                    points = points + 10
                else:
                    print("grid %d incorrect" % (i + 1))  # modify it could fit 3 by 3 soduku'''

                if args.explain:
                    print('explain:')

                    for each_step in explanation:
                        print(each_step)
            print("====================================")
            print("Test script complete, Total points: %d" % points)
        if args.profile:
            points = 0
            for (i, (grid)) in enumerate(grids):
                n_rows, n_cols = determine_grid_size(grid)
                print("Solving grid: %d" % (i + 1))  # modify it could fit 3 by 3 soduku
                num_attempts = 0

                # Calculate difficulty for each grid
                ratio = difficulty(grid, n_rows, n_cols)
                difficulties.append(ratio)

                # run the recursive solving program 5 times and get the average solving time
                while num_attempts <= 4:
                    start_time = time.time()
                    solution = solve(copy.deepcopy(grid), n_rows, n_cols, args.explain, args.hint)
                    elapsed_time = time.time() - start_time
                    Ttime.append(elapsed_time)
                    num_attempts += 1
                ave_time = sum(Ttime) / len(Ttime)
                average_time.append(ave_time)
                start_time = time.time()
                solution, explanation = solve(copy.deepcopy(grid), n_rows, n_cols, args.explain, args.hint)
                ave_time = time.time() - start_time

                print("The average time for the program to run 5 times: %f seconds" % ave_time)
                print(solution)
                if check_solution(solution, n_rows, n_cols):
                    print("grid %d correct" % (i + 1))  # modify it could fit 3 by 3 soduku
                    points = points + 10
                else:
                    print("grid %d incorrect" % (i + 1))  # modify it could fit 3 by 3 soduku'''
                if args.explain:
                    print('explain:')

                    for each_step in explanation:
                        print(each_step)
            print("====================================")
            print("Test script complete, Total points: %d" % points)
            slope, intercept = np.polyfit(difficulties, average_time, 1)
            plt.scatter(difficulties, average_time)

            # Set title and axis labels
            plt.title('Difficulty vs. Average Time')
            plt.plot(difficulties, slope * np.array(difficulties) + intercept, label='Best fit line')
            plt.xlabel('difficulties')
            plt.ylabel('average_time (s)')
            plt.legend()
            plt.show()

    if output:
        start_time = time.time()
        solved_grid, explanation = solve(grid, n_rows, n_cols, args.explain, args.hint)
        elapsed_time = time.time() - start_time
        print(f"Solved grid {input_file}:\n", solved_grid)
        print("Solved in %f seconds" % elapsed_time)
        write_grid_to_file(solved_grid, output_file)

        if args.explain:
            print('explain:')
            for each_step in explanation:
                print(each_step)
            with open(output_file, 'a') as file:
                file.write('\n\n\nExplanation:\n\n\n')
                for each_step in explanation:
                    file.write(each_step + '\n')


if __name__ == "__main__":
    main()

grid1=[[1,0,3,4,5,6],
       [4,5,6,1,0,3],
       [0,3,4,5,6,1],
       [5,6,1,0,3,4],
       [3,4,5,6,1,0],
       [6,1,0,3,4,5]]
# 测试用数独，随便写的

def solve(grid, n_rows, n_cols):
    n = n_rows*n_cols
    def start(grid):
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    return x, y
        return False, False


    def next(grid, x, y):
        for next_y in range(y + 1, n):
            if grid[x][next_y] == 0:
                return x, next_y
        for next_x in range(x + 1, n):
            for next_y in range(0, n):
                if grid[next_x][next_y] == 0:
                    return next_x, next_y
        return -1, -1


    def value(grid, x, y):
        i, j = x // n_cols, y // n_rows
        M = [grid[i * n_cols + r][j * n_rows + c] for r in range(n_cols) for c in range(n_rows)]
        v = set([x for x in range(1, n+1)]) - set(M) - set(grid[x]) - set(list(zip(*grid))[y])

        return list(v)


    def jie(grid, x, y):
        for grid[x][y] in value(grid, x, y):
            next_x, next_y = next(grid, x, y)
            if next_y == -1:
                return True
            elif jie(grid, next_x, next_y):
                return True
            else:
                grid[x][y] = 0


    def sudoku(grid):
        x, y = start(grid)
        jie(grid, x, y)
        print(grid)


    sudoku(grid)

solve(grid1,3,2)
#后续测试需要按照这个格式输入（grid，n_rows,n_cols)

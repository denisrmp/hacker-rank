# https://www.hackerrank.com/challenges/bomber-man


def explode_field(r, c, grid):
    new_grid = [list('O' * c) for _ in range(r)]
    for irow in range(r):
        for icol in range(c):
            if grid[irow][icol] == 'O':
                new_grid[irow][icol] = '.'
                if icol - 1 >= 0:
                    new_grid[irow][icol - 1] = '.'
                if icol + 1 < c:
                    new_grid[irow][icol + 1] = '.'
                if irow - 1 >= 0:
                    new_grid[irow - 1][icol] = '.'
                if irow + 1 < r:
                    new_grid[irow + 1][icol] = '.'
    return [''.join(row) for row in new_grid]


def bomber_man(r, c, n, grid):
    if n <= 1:
        return '\n'.join(grid)
    elif n % 2 == 0:
        return '\n'.join(['O' * c] * r)
    elif (n - 1) % 4 != 0:
        return '\n'.join(explode_field(r, c, grid))
    else:
        grid2 = explode_field(r, c, grid)
        return '\n'.join(explode_field(r, c, grid2))


r, c, n = [int(i) for i in input().split()]
grid = []
for _ in range(r):
    grid.append(input())

print(bomber_man(r, c, n, grid))

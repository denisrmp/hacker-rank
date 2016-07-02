# https://www.hackerrank.com/challenges/cavity-map


def is_cavity(last_row, row, next_row, idx):
    if (idx == 0) or (idx == len(row) - 1):
        return False
    else:
        return row[idx] > row[idx - 1] and row[idx] > row[idx + 1] \
               and row[idx] > last_row[idx] and row[idx] > next_row[idx]


n = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = str(input().strip())
    grid.append(grid_t)

print(grid[0])

if len(grid) > 2:
    for i in range(1, len(grid[1:-1]) + 1):
        print("".join(
            ['X' if is_cavity(grid[i - 1], grid[i], grid[i + 1], j) else grid[i][j] for j in range(len(grid[i]))]))

if len(grid) > 1:
    print(grid[-1])

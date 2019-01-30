# https://www.hackerrank.com/challenges/p1-paper-cutting


def solve(n, m):
    return (m - 1) + (n - 1) * m

n, m = [int(x) for x in input().strip().split()]
print(solve(n, m))

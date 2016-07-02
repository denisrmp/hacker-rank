# https://www.hackerrank.com/challenges/chocolate-feast


def tickets2chocolate(n, m):
    return 0 if n // m < 1 else n // m + tickets2chocolate(n // m + n % m, m)


t = int(input().strip())
for a0 in range(t):
    n, c, m = map(int, input().strip().split(' '))
    print(n // c + tickets2chocolate(n // c, m))

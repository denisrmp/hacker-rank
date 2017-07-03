# https://www.hackerrank.com/challenges/between-two-sets/


def gcd(x, y):
    return x if (y == 0) else gcd(y, x % y)


def lcm(x, y):
    return x * y / gcd(x, y)


def list_lcm(a):
    return a[0] if len(a) == 1 else lcm(a[0], list_lcm(a[1:]))


def check_factor(x, b):
    return len(b) == len([y for y in b if y % x == 0])


def between_sets(a, b):
    x = int(list_lcm(a))
    return sum(True for y in range(x, b[0] + 1, x) if check_factor(y, b))


_ = input().strip().split(' ')
a = [int(a) for a in input().strip().split(' ')]
b = [int(b) for b in input().strip().split(' ')]
print(between_sets(a, b))

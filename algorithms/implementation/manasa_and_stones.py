# https://www.hackerrank.com/challenges/manasa-and-stones


def manasa_and_stones(n, a, b):
    values = sorted(set([a * i + b * (n - i - 1) for i in range(n)]))
    return " ".join(map(str, values))


t = int(input())

for i in range(t):
    n = int(input())
    a = int(input())
    b = int(input())

    print(manasa_and_stones(n, a, b))

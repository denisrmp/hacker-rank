# https://www.hackerrank.com/challenges/flatland-space-stations


def flatland_space_stations(n, c):
    d1 = c[0]
    d2 = 0 if len(c) < 2 else max(a - b for a, b in zip(c[1:], c[:-1])) // 2
    d3 = n - c[-1] - 1
    return max(d1, d2, d3)


n, _ = [int(i) for i in input().split()]
c = sorted(int(i) for i in input().split())

print(flatland_space_stations(n, c))

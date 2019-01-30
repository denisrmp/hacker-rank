# https://www.hackerrank.com/challenges/utopian-tree


cache = {0:1, 1:2, 2:3, 3:6, 4:7}
max_n = 4


def get_how_tall(n):
    for i in range(max_n, n + 1):
        if i % 2 == 0: # adding season
            cache[i] = cache[i - 1] + 1
        else: # doubling season
            cache[i] = cache[i - 1] * 2
    return cache[n]


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    if n in cache:
        print(cache[n])
    else:
        print(get_how_tall(n))

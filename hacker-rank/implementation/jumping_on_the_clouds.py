# https://www.hackerrank.com/challenges/jumping-on-the-clouds


def jumping_on_the_clouds(n, c):
    jumps = 0
    i = 0

    # first cloud is not jumpable, so n - 1
    while i < n - 1:
        if i + 2 < n and c[i + 2]:
            i += 1
        else:
            i += 2
        jumps += 1

    return jumps


n = int(input().strip())
c = [int(i) for i in input().split(' ')]
print(jumping_on_the_clouds(n, c))

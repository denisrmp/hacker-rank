# https://www.hackerrank.com/challenges/minimum-distances


def minimum_distances(A):
    min_dist = -1

    for i, a_i in enumerate(A):
        if min_dist == 1:
            break
        for j, a_j in enumerate(A[(i + 1):]):
            if min_dist != -1 and j + 1 > min_dist:
                break
            elif a_i == a_j:
                min_dist = j + 1
                break

    return min_dist


n = int(input().strip())
A = [int(a) for a in input().strip().split(' ')]

print(minimum_distances(A))

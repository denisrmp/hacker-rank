# https://www.hackerrank.com/challenges/absolute-permutation


def absolute_permutation(n, k):
    if not k:
        return ' '.join(str(i) for i in range(1, n + 1))
    elif n % (k * 2) != 0:
        return -1
    else:
        cicle = [k + i for i in range(1, k + 1)] + [i for i in range(1, k + 1)]
        ans = [2 * k * m + i for m in range(n // (k * 2)) for i in cicle]
        return ' '.join(str(i) for i in ans)


T = int(input())
for _ in range(T):
    n, k = [int(i) for i in input().split()]
    print(absolute_permutation(n, k))

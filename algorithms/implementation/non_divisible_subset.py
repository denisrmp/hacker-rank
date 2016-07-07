# https://www.hackerrank.com/challenges/non-divisible-subset

from collections import Counter
from math import ceil


def non_divisible_subset(s, k):
    size = 0
    counts = Counter(s)
    for i in range(ceil((k + 1) / 2)):
        if (i == 0 and counts[i]) or (i == k / 2 and counts[i]):
            size += 1
        else:
            size += max(counts[k - i], counts[i])

    return size


n, k = [int(x) for x in input().split(' ')]
s = [int(x) % k for x in input().split(' ')]

print(non_divisible_subset(s, k))

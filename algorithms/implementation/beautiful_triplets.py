# https://www.hackerrank.com/challenges/beautiful-triplets


def find_next(d, seq, i):
    if i < 0 or seq[-1] - seq[i] < d:
        return -1

    for j in range(i + 1, len(seq)):
        diff = seq[j] - seq[i]
        if diff == d:
            return j
        elif diff > d:
            return -1


def beautiful_triplets(n, d, seq):
    return sum(find_next(d, seq, find_next(d, seq, i)) != -1 for i in range(n - 2))


n, d = [int(i) for i in input().split()]
seq = [int(i) for i in input().split()]
print(beautiful_triplets(n, d, seq))

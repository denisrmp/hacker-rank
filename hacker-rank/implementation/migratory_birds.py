# https://www.hackerrank.com/challenges/migratory-birds


def migratory_birds(arr):
    counters = [0, 0, 0, 0, 0]
    for i in arr:
        counters[i - 1] = counters[i - 1] + 1
    return counters.index(max(counters)) + 1

_ = input()
arr = [int(x) for x in input().strip().split()]
print(migratory_birds(arr))

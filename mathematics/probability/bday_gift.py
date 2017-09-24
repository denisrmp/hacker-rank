# https://www.hackerrank.com/challenges/bday-gift


def choose(arr, group_size):
    if len(arr) < group_size:
        return []
    elif len(arr) == group_size:
        return arr



def bday_gift(arr):
    return sum(sum(x) for i from range(0, len(arr))
    for x in choose(arr, i)) / pow(len(arr), 2)


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

bday_gift(arr)

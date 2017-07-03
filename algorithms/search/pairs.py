# https://www.hackerrank.com/challenges/pairs


a, b = [int(x) for x in input().split()]
arr = sorted([int(x) for x in input().split()])

c, i, j = 0, 0, 1
while i < a and j < a:
    diff = arr[j] - arr[i]
    if diff == b:
        c = c + 1
        i = i + 1
        j = j + 1
    elif diff > b:
        i = i + 1
    else:
        j = j + 1

print(c)

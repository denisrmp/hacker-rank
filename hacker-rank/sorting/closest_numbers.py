# https://www.hackerrank.com/challenges/closest-numbers


size = int(input())
arr = [int(x) for x in input().split()]
arr = sorted(arr)

closers = []
dist = 10000000000
for i in range(size - 1):
    if abs(arr[i] - arr[i + 1]) < dist:
        closers = []
        dist = abs(arr[i] - arr[i + 1])

    if abs(arr[i] - arr[i + 1]) == dist:
        closers.append(arr[i])
        closers.append(arr[i + 1])

print(' '.join([str(x) for x in closers]))

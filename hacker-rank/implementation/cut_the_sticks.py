# https://www.hackerrank.com/challenges/cut-the-sticks


n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))

while len(arr) > 0:
    arr2 = []
    for e in arr:
        e -= min(arr)
        if e > 0:
            arr2.append(e)
    print(len(arr))
    arr = arr2

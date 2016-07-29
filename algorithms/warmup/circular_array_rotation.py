# https://www.hackerrank.com/challenges/circular-array-rotation


n, k, q = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

# rotate k times
bm = b[-k % n:] + b[:-k % n]

for _ in range(q):
    i = int(input())
    print(bm[i])

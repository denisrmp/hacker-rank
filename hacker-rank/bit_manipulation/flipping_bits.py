# https://www.hackerrank.com/challenges/flipping-bits


n = int(input())
for i in range(n):
    ins = int(input())
    print(~ins & 0xffffffff)

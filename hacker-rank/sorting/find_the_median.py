# https://www.hackerrank.com/challenges/find-the-median


l = int(input())
arr = [int(x) for x in input().split()]
arr = sorted(arr)

print(arr[l // 2])

# https://www.hackerrank.com/challenges/service-lane


(n, t) = map(int, input().strip().split(' '))
width = list(map(int, input().strip().split(' ')))

for a0 in range(t):
    i, j = map(int, input().strip().split(' '))
    print(min(width[i:(j+1)]))

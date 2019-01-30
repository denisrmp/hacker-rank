# https://www.hackerrank.com/challenges/sherlock-and-squares


from math import sqrt, floor

t = int(input().strip())

for a0 in range(t):
    a, b = map(int, input().strip().split(' '))
    print(int(floor(sqrt(b)) - floor(sqrt(a - 1))))

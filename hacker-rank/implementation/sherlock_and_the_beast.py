# https://www.hackerrank.com/challenges/sherlock-and-the-beast

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n < 8 and not (n % 3 == 0 or n % 5 == 0):
        print('-1')
    else:
        x = (0, 2, 1)[n % 3] * 5
        print('5' * (n - x) + ('3' * x))

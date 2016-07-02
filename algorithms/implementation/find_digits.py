# https://www.hackerrank.com/challenges/find-digits


def find_digits(n):
    count = 0
    for c in str(n):
        d = int(c)
        if d != 0 and n % d == 0:
            count += 1
    return count


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(find_digits(n))
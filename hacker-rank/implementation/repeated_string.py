# https://www.hackerrank.com/challenges/repeated-string


LETTER = 'a'


def repeated_string(s, n):
    if len(s) == 0:
        return 0
    return s.count('a') * (n // len(s)) + s[:(n % len(s))].count('a')


s = input().strip()
n = int(input().strip())
print(repeated_string(s, n))

# https://www.hackerrank.com/challenges/kaprekar-numbers


def is_kaprekar(i):
    d = len(str(i))
    s = str(i ** 2)
    a, b = int(s[-d:]), int(s[:-d] or '0')
    return a + b == i


def kaprekar_numbers(p, q):
    return [i for i in range(p, q + 1) if is_kaprekar(i)]


p = int(input())
q = int(input())
numbers = kaprekar_numbers(p, q)

if numbers:
    print(' '.join(map(str, numbers)))
else:
    print('INVALID RANGE')

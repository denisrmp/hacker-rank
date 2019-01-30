# https://www.hackerrank.com/challenges/kangaroo


def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return x1 == x2
    else:
        if x1 < x2:
            x2, v2, x1, v1 = x1, v1, x2, v2
        res = (x2 - x1)/(v1 - v2)
        return res.is_integer() and res > 0


x1, v1, x2, v2 = map(float, input().strip().split(' '))
print('YES' if kangaroo(x1, v1, x2, v2) else 'NO')

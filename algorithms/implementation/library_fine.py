# https://www.hackerrank.com/challenges/library-fine


def numcat(n1, n2, n3):
    return '%d%d%d' % (n1, n2, n3)


def is_late(actual, expec):
    return numcat(actual['year'], actual['month'], actual['day']) > numcat(expec['year'], expec['month'], expec['day'])


def library_fine(actual, expected):
    if not is_late(actual, expected):
        return 0
    elif actual['year'] > expected['year']:
        return 10000
    elif actual['month'] > expected['month']:
        return 500 * (actual['month'] - expected['month'])
    else:
        return 15 * (actual['day'] - expected['day'])


d1, m1, y1 = map(int, input().strip().split(' '))
d2, m2, y2 = map(int, input().strip().split(' '))

print(library_fine({'day': d1, 'month': m1, 'year': y1}, {'day': d2, 'month': m2, 'year': y2}))

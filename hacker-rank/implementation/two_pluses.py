# https://www.hackerrank.com/challenges/two-pluses

import re


def prepare_matcher(c, size):
    if size == 0:
        return 'G'
    regex = ('G[\s\S]{%d}' * size) % tuple([c] * (size - 1) + [c - size])
    regex += 'G{%d})G(?=G{%d}' % (size, size)
    regex += ('[\s\S]{%d}G' * size) % tuple([c - size] + [c] * (size - 1))
    return '(?<=' + regex + ')'


def row_range(row, c):
    if c['row'] == row:
        return set(range(c['col'] - c['size'], c['col'] + c['size'] + 1))
    elif c['row'] - c['size'] <= row <= c['row'] + c['size']:
        return {c['col']}
    else:
        return {}


def row_collide(row, c1, c2):
    r1 = row_range(row, c1)
    for i in row_range(row, c2):
        if i in r1:
            return True
    return False


def intersect(c1, c2):
    for row in range(c2['row'] - c2['size'], c2['row'] + c2['size'] + 1):
        if row_collide(row, c1, c2):
            return True
    return False


def first_diff(c, cs):
    for c2 in cs:
        if not intersect(c, c2):
            return c2


def to_plus(m, s, ncol):
    center = m.span()[0]
    row = center // (ncol + 1)
    col = center - (row * (ncol + 1))
    return {'row': row, 'col': col, 'size': s}


def two_pluses(r, c, grid):
    smax = min(r, c) // 2

    centers = [to_plus(m, s, c) for s in range(smax, -1, -1)
               for m in re.finditer(prepare_matcher(c, s), grid)]

    for i, c1 in enumerate(centers):
        c2 = first_diff(c1, centers[(i + 1):])
        if c2:
            return (1 + (c1['size'] * 4)) * (1 + (c2['size'] * 4))

    return 0


r, c = [int(i) for i in input().split()]
grid = '|'.join([input() for _ in range(r)])
print(two_pluses(r, c, grid))

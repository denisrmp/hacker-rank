# https://www.hackerrank.com/challenges/the-grid-search

import re

t = int(input().strip())
for a0 in range(t):
    (mrow, mcol) = map(int, input().split())
    matrix = '|'.join([input() for _ in range(mrow)])

    (prow, pcol) = map(int, input().split())
    pattern = re.compile(('.{' + str(mcol - pcol + 1) + '}').join([input() for _ in range(prow)]))

    print('YES' if pattern.search(matrix) else 'NO')

# https://www.hackerrank.com/challenges/new-year-chaos

from collections import deque


def new_year_chaos(n, q):
    acc = 0
    expect = list(range(1, n + 1))
    while len(q):
        iof = expect.index(q[0])
        if iof > 2:
            return 'Too chaotic'
        else:
            acc += iof
            expect.remove(q[0])
            q.popleft()

    return acc


T = int(input())
for _ in range(T):
    n = int(input())
    q = deque((int(i) for i in input().split()), n)
    print(new_year_chaos(n, q))

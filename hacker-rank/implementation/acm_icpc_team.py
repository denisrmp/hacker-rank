# https://www.hackerrank.com/challenges/acm-icpc-team


def union(p1, p2):
    return [t1 | t2 for t1, t2 in zip(p1, p2)]


def acm_icpc_team(persons):
    max_t, max_qty = 0, 0
    for i, p1 in enumerate(persons):
        for j, p2 in enumerate(persons[(i + 1):], i + 1):
            t = sum(union(p1, p2))
            if t == max_t:
                max_qty += 1
            elif t > max_t:
                max_t, max_qty = t, 1
    return max_t, max_qty


n, m = [int(x) for x in input().split(' ')]
persons = [[int(x) for x in list(input())] for p in range(n)]
print("%d\n%d" % (acm_icpc_team(persons)))

# https://www.hackerrank.com/challenges/almost-sorted


ORDERED = 'yes'
SWAP = 'yes\nswap {} {}'
REVERSE = 'yes\nreverse {} {}'
IMPOSSIBLE = 'no'


def get_misplaced(ds):
    misplaced = []
    for i, d in enumerate(ds[1:], 1):
        if d < ds[i - 1]:
            misplaced.append(i - 1)
    return misplaced


def handle_swap(i, ds):
    if len(ds) == 2:
        return SWAP.format(1, 2)
    to = next((k - 1 for k, v in enumerate(ds) if v > ds[i]), None)
    if to is None or to < i or (i > 0 and ds[to] < ds[i - 1]):
        return IMPOSSIBLE
    else:
        return SWAP.format(i + 1, to + 1)


def is_seq(l):
    for k, v in enumerate(l[1:], 1):
        if v - l[k - 1] != 1:
            return False
    return True


def reverse_works(ids, ds):
    return len(ds) == ids[-1] + 1 or ds[ids[0]] < ds[ids[-1] + 2]


def is_reversable(ids, ds):
    return len(ds) > 2 and is_seq(ids) and reverse_works(ids, ds)


def almost_sorted(ds):
    ids = get_misplaced(ds)
    if not ids:
        return ORDERED
    elif len(ids) == 1:
        return handle_swap(ids[0], ds)
    elif len(ids) == 2:
        return SWAP.format(ids[0] + 1, ids[1] + 2)
    elif is_reversable(ids, ds):
        return REVERSE.format(ids[0] + 1, ids[-1] + 2)
    else:
        return IMPOSSIBLE

n = int(input())
ds = [int(i) for i in input().strip().split()]
print(almost_sorted(ds))

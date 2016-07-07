# https://www.hackerrank.com/challenges/fair-rations


def give_loaves(B):
    B[0] += 1
    B[1] += 1
    return B


def trim_odd(B):
    while len(B) > 0 and B[0] % 2 == 0:
        B.pop(0)
    while len(B) > 0 and B[-1] % 2 == 0:
        B.pop()
    return B


def fair_rations(B):
    loaves = 0

    while True:
        B = trim_odd(B)
        if len(B) == 0:
            return loaves
        elif len(B) == 1:
            return 'NO'
        else:
            B = give_loaves(B)
            loaves += 2


n = int(input())
B = [int(b) for b in input().split(' ')]
print(fair_rations(B))

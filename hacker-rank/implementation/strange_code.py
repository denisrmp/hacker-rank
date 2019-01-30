# https://www.hackerrank.com/challenges/strange-code

from math import log, floor


INITIAL_CYCLE_SIZE = 3


def strange_code(t):
    cycle = lambda x: floor(log((-1 + INITIAL_CYCLE_SIZE + x) / (INITIAL_CYCLE_SIZE / 2), 2))
    uncycle = lambda c: 1 - INITIAL_CYCLE_SIZE + (INITIAL_CYCLE_SIZE * 2 ** c) / 2
    return int(2 ** cycle(t) * (INITIAL_CYCLE_SIZE / 2) - t + uncycle(cycle(t)))


t = int(input())
print(strange_code(t))

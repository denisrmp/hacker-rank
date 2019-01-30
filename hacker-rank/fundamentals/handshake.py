# https://www.hackerrank.com/challenges/handshake


def handshake(n):
    return n * (n - 1) / 2


T = int(input().strip())
for a0 in range(T):
    N = int(input().strip())
    print(int(handshake(N)))

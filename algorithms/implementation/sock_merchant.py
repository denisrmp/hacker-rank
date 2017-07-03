# https://www.hackerrank.com/challenges/sock-merchant


def sock_merchant(socks):
    sock_map = {}
    for sock in socks:
        if sock in sock_map:
            sock_map[sock] += 1
        else:
            sock_map[sock] = 1

    counter = 0
    for color, qty in sock_map.items():
        counter += qty // 2

    return counter


n = int(input())
c = [int(i) for i in input().strip().split(' ')]
print(sock_merchant(c))

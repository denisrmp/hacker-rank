# https://www.hackerrank.com/challenges/taum-and-bday


def taum_and_bday(b, w, x, y, z):
    x_ = min(x, y + z)
    y_ = min(y, x + z)
    return b * x_ + w * y_


t = int(input().strip())
for a0 in range(t):
    b, w = [int(i) for i in input().strip().split(' ')]
    x, y, z = [int(i) for i in input().strip().split(' ')]
    print(taum_and_bday(b, w, x, y, z))

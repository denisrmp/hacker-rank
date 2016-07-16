# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited


def jumping_on_the_clouds_revisited(n, k, clouds, E):
    jumps = (n // k) * (1 + (- n % k))
    return E - jumps - sum([clouds[i * k % n] * 2 for i in range(jumps)])


n, k = map(int, input().split())
clouds = [int(a) for a in input().split(' ')]
print(jumping_on_the_clouds_revisited(n, k, clouds, E=100))

# https://www.hackerrank.com/challenges/divisible-sum-pairs


def divisible_sum_pairs(n, k, a):
    return len([True for j in range(n - 1, 0, -1) for i in range(j) if not (a[i] + a[j]) % k])


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
print(divisible_sum_pairs(n, k, a))

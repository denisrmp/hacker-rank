# https://www.hackerrank.com/challenges/compare-the-triplets

a = [int(i) for i in input().split(' ')]
b = [int(i) for i in input().split(' ')]

a_score = 0
b_score = 0
for a_i, b_i in zip(a, b):
    if a_i > b_i:
        a_score += 1
    elif b_i > a_i:
        b_score += 1

print("%d %d" % (a_score, b_score))

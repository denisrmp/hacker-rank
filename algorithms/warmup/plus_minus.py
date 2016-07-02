# https://www.hackerrank.com/challenges/plus-minus

n = int(input().strip())
arr = map(int, input().strip().split(' '))

pos, neg, zeros = 0., 0., 0.
for a in arr:
    if a == 0:
        zeros += 1
    elif a > 0:
        pos += 1
    elif a < 0:
        neg += 1

print(pos/n)
print(neg/n)
print(zeros/n)

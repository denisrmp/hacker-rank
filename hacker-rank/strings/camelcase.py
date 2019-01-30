# https://www.hackerrank.com/challenges/camelcase


s = input().strip()
cnt = 1
for c in list(s):
    if c.isupper():
        cnt = cnt + 1

print(cnt)

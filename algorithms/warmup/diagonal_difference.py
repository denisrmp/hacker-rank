# https://www.hackerrank.com/challenges/diagonal-difference

n = int(input().strip())

primary = 0
secondary = 0

for a_i in range(n):
  a_temp = list(map(int, input().strip().split(' ')))
  primary += a_temp[a_i]
  secondary += a_temp[- a_i - 1]

print(abs(primary - secondary))

# https://www.hackerrank.com/challenges/angry-professor

t = int(input().strip())
for a0 in range(t):
  n, k = map(int, input().strip().split(' '))
  a = list(map(int, input().strip().split(' ')))
  print('YES' if not sum([i <= 0 for i in a[0:n]]) >= k else 'NO')

# https://www.hackerrank.com/challenges/save-the-prisoner

cases = int(input())

def save_the_prisoner(n, m, s):
  return (m + s - 1) % n or n

for case in range(cases):
  (n, m, s) = map(int, input().split())
  print(save_the_prisoner(n, m, s))

# https://www.hackerrank.com/challenges/funny-string

def funny_string(s):
    z = s[::-1]
    for i in range(len(s) - 1):
        if abs(ord(s[i]) - ord(s[i + 1])) != abs(ord(z[i]) - ord(z[i + 1])):
            return 'Not Funny'
    return 'Funny'


q = int(input())
for _ in range(q):
    s = input()
    print(funny_string(s))

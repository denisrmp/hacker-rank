# https://www.hackerrank.com/challenges/bigger-is-greater


def bigger_is_greater(string):
    s = list(string)
    if len(set(s)) == 1:
        return 'no answer'
    else:
        last = s[-1]
        for i, c in reversed(list(enumerate(s))):
            if c > last:
                last = c
            elif c < last:
                sub = s.index(min(char for char in s[(i + 1):] if char > s[i]), i + 1)
                s[i], s[sub] = s[sub], s[i]
                return ''.join(s[:(i + 1)] + sorted(s[(i + 1):]))
    return 'no answer'


n = int(input())
for _ in range(n):
    s = input()
    print(bigger_is_greater(s))

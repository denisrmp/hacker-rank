# https://www.hackerrank.com/challenges/balanced-brackets

def is_balanced(s):
    pair_of = {')':'(', ']':'[', '}':'{'}
    stack = [s[0]]
    for ch in s[1:]:
        if ch in ['(', '[', '{']:
            stack.append(ch)
        elif len(stack) == 0 or stack.pop() != pair_of[ch]:
            return 'NO'

    return 'YES' if len(stack) == 0 else 'NO'


t = int(input().strip())
for _ in range(t):
    s = input().strip()
    print(is_balanced(s))

# https://www.hackerrank.com/challenges/sherlock-and-anagrams


def set_from_index(string, idx, size):
    si = []
    for i in range(size):
        si.append(string[idx + i])
    return ''.join(sorted(si))


def compute_set_size(s, size):
    sets = {}
    count = 0
    for i in range(len(s)):
        if i + size > len(s):
            break

        si = set_from_index(s, i, size)

        if si in sets:
            count = count + sets[si]
            sets[si] = sets[si] + 1
        else:
            sets[si] = 1
    return count


def sherlock_and_anagrams(s):
    count = 0
    s = list(s)
    for i in range(len(s)):
        count = count + compute_set_size(s, i + 1)
    return count


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    print(sherlock_and_anagrams(s))

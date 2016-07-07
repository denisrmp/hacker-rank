# https://www.hackerrank.com/challenges/equal-stacks


def equal_stacks(stacks):
    stacks_size = [sum(stack) for stack in stacks]
    while len(set(stacks_size)) > 1:
        higher = stacks_size.index(max(stacks_size))
        poped = stacks[higher].pop(0)
        stacks_size[higher] -= poped

    return stacks_size[0]


n1, n2, n3 = map(int, input().strip().split(' '))
s1 = [int(x) for x in input().strip().split(' ')]
s2 = [int(x) for x in input().strip().split(' ')]
s3 = [int(x) for x in input().strip().split(' ')]

print(equal_stacks([s1, s2, s3]))

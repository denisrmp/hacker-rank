# https://www.hackerrank.com/challenges/the-hurdle-race/


def hurdle_race(max_jump, heights):
    return max(0, max(heights) - max_jump)


_, k = [int(i) for i in input().strip().split(' ')]
heights = [int(i) for i in input().strip().split(' ')]
print(hurdle_race(k, heights))

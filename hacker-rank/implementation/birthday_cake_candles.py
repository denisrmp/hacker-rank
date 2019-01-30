# https://www.hackerrank.com/challenges/birthday-cake-candles


def birthday_cake_candles(heights):
    return heights.count(max(heights))


_ = input()
heights = [int(h) for h in input().strip().split()]
print(birthday_cake_candles(heights))

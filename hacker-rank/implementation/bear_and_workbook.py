# https://www.hackerrank.com/challenges/bear-and-workbook

from math import ceil

chaps, maxppp = map(int, input().split())
probs = map(int, input().split())

book_page = 1
acc = 0

for prob in probs:
    for chap_page in range(1, ceil(prob / maxppp) + 1):
        llim = 1 + (maxppp * (chap_page - 1))
        ulim = min(prob, maxppp * chap_page)
        if llim <= book_page <= ulim:
            acc += 1
        book_page += 1

print(acc)

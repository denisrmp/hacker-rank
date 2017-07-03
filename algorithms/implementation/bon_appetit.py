# https://www.hackerrank.com/challenges/bon-appetit


def bon_appetit(k, prices, charged):
    change = charged - (sum(prices) - prices[k])//2
    if change == 0:
        return 'Bon Appetit'
    else:
        return change


n, k = [int(i) for i in input().split()]
prices = [int(i) for i in input().split()]
charged = int(input())
print(bon_appetit(k, prices, charged))

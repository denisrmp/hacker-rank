# https://www.hackerrank.com/challenges/2d-array

def sum_hourglass(arr, i, j):
    return arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + \
           arr[i + 1][j + 1] + \
           arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]


def two_d_array(arr):
    return max(sum_hourglass(arr, i, j)
               for i in range(len(arr) - 2)
               for j in range(len(arr[0]) - 2))


arr = [[int(x) for x in input().split()] for _ in range(6)]
print(two_d_array(arr))

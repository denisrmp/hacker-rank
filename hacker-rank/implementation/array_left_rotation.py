# https://www.hackerrank.com/challenges/array-left-rotation/


def rotate(arr, rotations):
    r = rotations % len(arr)
    return arr[r:] + arr[:r]


_, rotations = [int(i) for i in input().strip().split()]
arr = input().strip().split()
print(' '.join(rotate(arr, rotations)))

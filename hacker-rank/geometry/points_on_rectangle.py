# https://www.hackerrank.com/challenges/points-on-rectangle

def points_on_rectangle(px, py):
    min_x, max_x = min(px), max(px)
    min_y, max_y = min(py), max(py)
    for i in range(len(px)):
        if px[i] != min_x and px[i] != max_x and py[i] != min_y and py[i] != max_y:
            return 'NO'
    return 'YES'


cases = int(input())
for _ in range(cases):
    qty_points = int(input())
    px, py = [], []
    for _ in range(qty_points):
        x, y = [int(z) for z in input().split()]
        px.append(x)
        py.append(y)
    print(points_on_rectangle(px, py))

BOTTOM = 0
TOP = 2
LEFT = 1
RIGHT = 3


def calc_total_area(rectangles):
    rectangles = tuple(set(rectangles))  # eliminate duplicates
    total_area = 0
    for rectangle in rectangles:
        total_area = total_area + (rectangle[TOP] - rectangle[BOTTOM]) * (rectangle[RIGHT] - rectangle[LEFT])
    if len(rectangles) <= 1:
        return total_area
    else:
        intersection_rectangles = get_intersections(rectangles)
        return total_area - calc_total_area(intersection_rectangles)


def get_intersections(rectangles):
    intersections = []
    for i in xrange(0, len(rectangles) - 1):
        for j in xrange(i + 1, len(rectangles)):
            if overlap(rectangles[i], rectangles[j]):
                intersections.append(calc_intersection(rectangles[i], rectangles[j]))
    return intersections


def overlap(a, b):
    # from http://codereview.stackexchange.com/a/31529
    return range_overlap(a[LEFT], a[RIGHT], b[LEFT], b[RIGHT]) and range_overlap(a[BOTTOM], a[TOP], b[BOTTOM], b[TOP])


def range_overlap(a_min, a_max, b_min, b_max):
    return (a_min <= b_max) and (b_min <= a_max)


def calc_intersection(a, b):
    return max(a[LEFT], b[LEFT]), max(a[BOTTOM], b[BOTTOM]), min(a[RIGHT], b[RIGHT]), min(a[TOP], b[TOP])


def run():
    rectangles = []
    coordinates = raw_input().replace('\n', ' ').split()
    for i in xrange(0, int(coordinates[0])):
        rectangles.append(tuple([float(coordinates[x + (4 * i)]) for x in xrange(1, 5)]))
    print(calc_total_area(rectangles))

import os
from itertools import combinations
import shapely

def area(p0, p1):
    w = abs(p1[0] - p0[0]) + 1
    h = abs(p1[1] - p0[1]) + 1
    return w * h

def main1(points):
    return max([area(a, b) for a, b in combinations(points, 2)])

def main2(points):
    areas = [(area(a, b), a, b) for a, b in combinations(points, 2)]
    polygon = shapely.Polygon(points)
    for val, a, b in reversed(sorted(areas)):
        c = [b[0], a[1]]
        d = [a[0], b[1]]
        rectangle = shapely.Polygon([a, c, b, d])
        if polygon.covers(rectangle):
            return val
    return 0

def segment_is_outside_rectangle(a, b, left, right, top, bottom):
    if a[0] == b[0]: # Vertical
        return a[0] <= left or a[0] >= right or max(a[1], b[1]) <= top or min(a[1], b[1]) >= bottom
    else:
        assert(a[1] == b[1]) # horizontal
        return a[1] <= top or a[1] >= bottom or max(a[0], b[0]) <= left or min(a[0], b[0]) >= right

def polygon_surrounds_rectangle(poly, left, right, top, bottom):
    for i in range(len(poly)):
        j = (i + 1) % len(poly)
        if not segment_is_outside_rectangle(poly[i], poly[j], left, right, top, bottom):
            return False
    return True

def main2_alt(points):
    areas = [(area(a, b), a, b) for a, b in combinations(points, 2)]
    for val, a, b in reversed(sorted(areas)):
        left = min(a[0], b[0])
        right = max(a[0], b[0])
        top = min(a[1], b[1])
        bottom = max(a[1], b[1])
        if polygon_surrounds_rectangle(points, left, right, top, bottom):
            return val
    return 0

def parse_input(file_path):
    with open(file_path) as file:
        return [[int(x) for x in line.rstrip("\n").split(",")] for line in file.readlines()]
    return []

def print_result(challenge_n, ans, exp):
    print(f"Challenge {challenge_n}. Got: {ans}, expected: {exp}. {'PASS' if ans == exp else 'FAIL'}")

def main(file_path, exp1, exp2):
    points = parse_input(file_path)
    print(f"*** Input: {file_path}")
    print_result(1, main1(points), exp1)
    print_result(2, main2(points), exp2)
    print_result(2.1, main2_alt(points), exp2)

if __name__ == "__main__":
    main(os.path.dirname(__file__) + "/dummy_input.txt", 50, 24)
    main(os.path.dirname(__file__) + "/input.txt", 4767418746, 1461987144)


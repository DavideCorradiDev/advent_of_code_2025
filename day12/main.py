import os
import math

def definitely_works(area, shapes_count):
    return sum(shapes_count) <= math.prod(x // 3 for x in area)

def definitely_doesnt_work(shape_areas, area, shapes_count):
    return sum(count * shape_areas[i] for i, count in enumerate(shapes_count)) > math.prod(x for x in area)

def main1(input):
    shapes, areas = input
    shape_areas = [sum(1 if c == "#" else 0 for c in shape) for shape in shapes]
    definitely_working_count = 0
    maybe_working_count = 0
    definitely_not_working_count = 0
    for area, shapes_count in areas:
        if definitely_works(area, shapes_count):
            definitely_working_count += 1
        elif definitely_doesnt_work(shape_areas, area, shapes_count):
            definitely_not_working_count += 1
        else:
            maybe_working_count += 1
    if maybe_working_count != 0:
        print ("!!! Uh-oh, we actually need a proper algorithm here...")
        print(f"    Fits: {definitely_working_count}, doesn't: {definitely_not_working_count}, who knows: {maybe_working_count}")
    return definitely_working_count

def parse_shape(lines, start, count):
    return "".join(lines[start:(start+count)])

def parse_area(line):
    area_str, shapes_str = line.split(": ")
    area = tuple(map(int, area_str.split("x")))
    shapes_count = list(map(int, shapes_str.split(" ")))
    return (area, shapes_count)

def parse_input(file_path):
    with open(file_path) as file:
        shapes = []
        areas = []
        lines = file.readlines()
        i = 0
        while i < len(lines):
            if len(lines[i]) < 2:
                # Empty line.
                i += 1
                continue
            if lines[i][-2] == ":":
                # Start of shape.
                shapes.append(parse_shape(lines, i+1, 3))
                i += 4
            else:
                # Area line.
                areas.append(parse_area(lines[i]))
                i += 1
        return (shapes, areas)


def print_result(challenge_n, ans, exp):
    print(f"Challenge {challenge_n}. Got: {ans}, expected: {exp}. {'PASS' if ans == exp else 'FAIL'}")

def main(file_path, exp1):
    input = parse_input(file_path)
    print(f"*** Input: {file_path}")
    print_result(1, main1(input), exp1)

if __name__ == "__main__":
    main(os.path.dirname(__file__) + "/dummy_input.txt", 2)
    main(os.path.dirname(__file__) + "/input.txt", 472)


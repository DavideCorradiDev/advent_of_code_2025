import os

def is_value_in_ranges(v, ranges):
    for min, max in ranges:
        if v >= min and v < max:
            return True
    return False

def merge_ranges(ranges):
    assert(ranges)
    ranges.sort()
    merged = [ranges[0]]
    for i in range(1, len(ranges)):
        if ranges[i][0] <= merged[-1][1]:
            if ranges[i][1] > merged[-1][1]:
                merged[-1] = (merged[-1][0], ranges[i][1])
        else:
            merged.append(ranges[i])
    return merged

def main1(ranges, values):
    return sum(1 for v in values if is_value_in_ranges(v, ranges))

def main2(ranges):
    return sum([max - min for min, max in merge_ranges(ranges)])

def test():
    assert(merge_ranges([(8, 12), (3, 8)]) == [(3, 12)])
    assert(merge_ranges([(8, 12), (8, 12)]) == [(8, 12)])
    assert(merge_ranges([(8, 12), (3, 6), (6, 8)]) == [(3, 12)])
    assert(merge_ranges([(8, 12), (9, 11)]) == [(8, 12)])
    print("*** Unit tests - PASSED")

def parse_input(file_path):
    with open(file_path) as file:
        lines = [line.rstrip() for line in file.readlines()]

        ranges = []
        i = 0
        while i < len(lines) and lines[i]:
            min, max = lines[i].split("-")
            assert(max >= min)
            ranges.append((int(min), int(max) + 1))
            i += 1

        i += 1
        values = []
        while i < len(lines):
            values.append(int(lines[i]))
            i += 1

    return (ranges, values)

def print_result(challenge_n, ans, exp):
    print(f"Challenge {challenge_n}. Got: {ans}, expected: {exp}. {'PASS' if ans == exp else 'FAIL'}")

def main(file_path, exp1, exp2):
    ranges, values = parse_input(file_path)
    print(f"*** Input: {file_path}")
    print_result(1, main1(ranges, values), exp1)
    print_result(2, main2(ranges), exp2)

if __name__ == "__main__":
    test()
    main(os.path.dirname(__file__) + "/dummy_input.txt", 3, 14)
    main(os.path.dirname(__file__) + "/input.txt", 664, 350780324308385)


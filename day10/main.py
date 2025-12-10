import os
from collections import deque
import numpy as np
import scipy

def configure_lights(target, switches):
    q = deque()
    q.append((tuple([0] * len(target)), 0))
    seen = set()
    while q:
        start, it = q.popleft()
        if start in seen:
            continue
        seen.add(start)
        for switch in switches:
            curr = tuple((x + (1 if i in switch else 0)) % 2 for i, x in enumerate(start))
            if curr == target:
                return it + 1
            q.append((curr, it + 1))
    return 0

def main1(input):
    return sum([configure_lights(target, switches) for target, switches, _ in input])

def configure_joltage(target, switches):
    coefficients = np.zeros((len(target), len(switches)))
    for c, switch in enumerate(switches):
        for r in switch:
            coefficients[r][c] = 1
    x = scipy.optimize.linprog([1]*len(switches), A_eq=coefficients, b_eq=target, bounds=(0, None), integrality=1)
    return x.fun

def main2(input):
    return sum([configure_joltage(target, switches) for _, switches, target in input])

def test():
    assert(configure_lights((0, 1, 1, 0), [[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]]) == 2)
    assert(configure_lights((0, 0, 0, 1, 0), [[0, 2, 3, 4], [2, 3], [0, 4], [0, 1, 2], [1, 2, 3, 4]]) == 3)
    assert(configure_lights((0, 1, 1, 1, 0, 1), [[0, 3, 4], [0, 1, 2, 4, 5]]) == 2)
    assert(configure_lights((0, 1, 1, 1, 0, 1), [[0, 1, 2, 3, 4], [0, 3, 4], [0, 1, 2, 4, 5], [1, 2]]) == 2)
    print("*** Unit tests. PASS")

def parse_input_line(line):
    line = line.rstrip("}\n").lstrip("[")
    lights, switches_and_joltages = line.split("] (")
    switches, joltages = switches_and_joltages.split(") {")

    lights = tuple([1 if c == "#" else 0 for c in lights])
    switches = [list(map(int, switch_set.split(","))) for switch_set in switches.split(") (")]
    joltages = list(map(int, joltages.split(",")))

    return(lights, switches, joltages) 

def parse_input(file_path):
    with open(file_path) as file:
        return [parse_input_line(line) for line in file.readlines()]
    return [((), [], ())]

def print_result(challenge_n, ans, exp):
    print(f"Challenge {challenge_n}. Got: {ans}, expected: {exp}. {'PASS' if ans == exp else 'FAIL'}")

def main(file_path, exp1, exp2):
    input = parse_input(file_path)
    print(f"*** Input: {file_path}")
    print_result(1, main1(input), exp1)
    print_result(2, main2(input), exp2)

if __name__ == "__main__":
    test()
    main(os.path.dirname(__file__) + "/dummy_input.txt", 7, 33)
    main(os.path.dirname(__file__) + "/input.txt", 505, 20002)


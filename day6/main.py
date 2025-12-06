import os
import math

def main1(file_path):
    values = []
    operators = []

    with open(file_path) as file:
        lines = [[v for v in line.split()] for line in file.readlines()]
        if lines:
            for _ in range(len(lines[0])):
                values.append([])
            for line in lines[:-1]:
                for i, v in enumerate(line):
                    values[i].append(int(v))
            operators = [sum if op == "+" else math.prod for op in lines[-1]]

    return sum([op(n) for op, n in zip(operators, values)])

def main2(file_path):
    values = []
    operators = []

    with open(file_path) as file:
        # Read characters into a grid.
        grid = [[c for c in line.rstrip()] for line in file.readlines()]

        # Calculate grid size.
        r_count = len(grid)
        c_count = max(map(len, grid))

        # Pad shorter rows.
        for row in grid:
            row += [" "] * (c_count - len(row))

        # Read transposed lines from the grid.
        lines = []
        for c in range(c_count):
            lines.append("")
            for r in range(r_count):
                lines[-1] += grid[r][c]
        
        # Parse operators and values from the lines.
        operators.append(None)
        values.append([])
        for line in lines:
            if line.isspace():
                operators.append(None)
                values.append([])
            elif not operators[-1]:
                operators[-1] = sum if line[-1] == "+" else math.prod
                values[-1].append(int(line[:-1]))
            else:
                values[-1].append(int(line))

    return sum([op(n) for op, n in zip(operators, values)])

def print_result(challenge_n, ans, exp):
    print(f"Challenge {challenge_n}. Got: {ans}, expected: {exp}. {'PASS' if ans == exp else 'FAIL'}")

def main(file_path, exp1, exp2):
    print(f"*** Input: {file_path}")
    print_result(1, main1(file_path), exp1)
    print_result(2, main2(file_path), exp2)

if __name__ == "__main__":
    main(os.path.dirname(__file__) + "/dummy_input.txt", 4277556, 3263827)
    main(os.path.dirname(__file__) + "/input.txt", 4076006202939, 7903168391557)


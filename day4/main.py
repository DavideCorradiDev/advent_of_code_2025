import os
from collections import deque

def count_adj_rolls(grid, x, y):
    count = 0
    sy = len(grid)
    sx = len(grid[0])
    for ox, oy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        nx = x + ox
        ny = y + oy   
        if nx < 0 or nx >= sx or ny < 0 or ny >= sy:
            continue
        if grid[ny][nx] == "@":
            count += 1
    return count

def main1(grid):
    ans = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "@" and count_adj_rolls(grid, x, y) < 4:
                ans += 1
    return ans

def main2(grid):
    ans = 0

    sy = len(grid)
    sx = len(grid[0])

    count_grid = []
    removables = deque()
    for y in range(sy):
        count_grid_row = []
        for x in range(sx):
            if grid[y][x] == "@":
                adj_rolls_count = count_adj_rolls(grid, x, y)
                count_grid_row.append(adj_rolls_count)
                if adj_rolls_count < 4:
                    removables.append((x, y))
            else:
                count_grid_row.append(-1)
        count_grid.append(count_grid_row)

    while removables:
        ans += 1
        (x, y) = removables.popleft()
        count_grid[y][x] = -1
        for ox, oy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nx = x + ox
            ny = y + oy   
            if nx < 0 or nx >= sx or ny < 0 or ny >= sy or count_grid[ny][nx] == -1:
                continue
            count_grid[ny][nx] -= 1
            if count_grid[ny][nx] < 4 and (nx, ny) not in removables:
                removables.append((nx, ny))

    return ans

def test():
    grid = parse_input(os.path.dirname(__file__) + "/dummy_input.txt")
    assert(count_adj_rolls(grid, 9, 8) == 4)
    print("*** Unit tests - PASSED")

def parse_input(file_path):
    with open(file_path) as file:
        grid = [line.rstrip() for line in file.readlines()]
    return grid

def print_result(challenge_n, ans, exp):
    print(f"Challenge {challenge_n}. Got: {ans}, expected: {exp}. {'PASS' if ans == exp else 'FAIL'}")

def main(file_path, exp1, exp2):
    grid = parse_input(file_path)
    print(f"*** Input: {file_path}")
    print_result(1, main1(grid), exp1)
    print_result(2, main2(grid), exp2)

if __name__ == "__main__":
    test()
    main(os.path.dirname(__file__) + "/dummy_input.txt", 13, 43)
    main(os.path.dirname(__file__) + "/input.txt", 1320, 8354)

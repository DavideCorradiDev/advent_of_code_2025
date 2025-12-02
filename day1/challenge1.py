import argparse
from pathlib import Path

def main(rotations):
    counter = 0
    accumulator = 50
    for (direction, amount) in rotations:
        accumulator = (accumulator + direction * amount) % 100
        if accumulator == 0:
            counter += 1
    return counter

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", type=Path)
    args = parser.parse_args()

    rotations = []
    with open(args.file_path) as file:
        for line in file.readlines():
            direction = -1 if line[0] == "L" else 1
            amount = int(line[1:])
            rotations.append((direction, amount))

    result = main(rotations)
    print(f"Result: {result}")


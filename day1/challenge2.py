import argparse
from pathlib import Path

def main(rotations):
    counter = 0
    accumulator = 50
    for (direction, amount) in rotations:
        if direction > 0:
            amount_to_zero = 100 - accumulator
        else:
            amount_to_zero = accumulator or 100
        accumulator = (accumulator + direction * amount) % 100
        counter += (amount - amount_to_zero) // 100 + 1
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


import argparse
from pathlib import Path

def check_repeat(x_str, p_len):
    x_len = len(x_str)
    if p_len == 0 or x_len // 2 < p_len or x_len % p_len != 0:
        return False
    for start in range(p_len, x_len, p_len):
        if x_str[:p_len] != x_str[start:start+p_len]:
            return False
    return True

def is_valid(x_str):
    for p_len in range(1, len(x_str) // 2 + 1):
        if check_repeat(x_str, p_len):
            return False
    return True

def test_check_repeat():
    assert(not check_repeat("0", 0))
    assert(not check_repeat("0", 1))

    assert(not check_repeat("1", 0))
    assert(not check_repeat("1212", 0))

    assert(not check_repeat("1", 1))
    assert(not check_repeat("1", 2))

    assert(not check_repeat("12", 1))
    assert(not check_repeat("12", 2))

    assert(check_repeat("11", 1))
    assert(not check_repeat("11", 2))

    assert(check_repeat("111", 1))
    assert(not check_repeat("111", 2))

    assert(not check_repeat("1212", 1))
    assert(check_repeat("1212", 2))
    assert(not check_repeat("1212", 3))

    assert(not check_repeat("868686", 1))
    assert(check_repeat("868686", 2))
    assert(not check_repeat("868686", 3))
    assert(not check_repeat("868686", 4))
    assert(not check_repeat("868686", 5))

    assert(not check_repeat("123123", 1))
    assert(not check_repeat("123123", 2))
    assert(check_repeat("123123", 3))
    assert(not check_repeat("123123", 4))
    assert(not check_repeat("123123", 5))

    assert(check_repeat("888888", 1))
    assert(check_repeat("888888", 2))
    assert(check_repeat("888888", 3))
    assert(not check_repeat("888888", 4))

    print("test_check_repeat: PASS")

def test_is_valid():
    assert(not is_valid("11"))
    assert(not is_valid("22"))
    assert(not is_valid("99"))
    assert(not is_valid("1010"))
    assert(not is_valid("1188511885"))
    assert(not is_valid("222222"))
    assert(not is_valid("446446"))
    assert(not is_valid("38593859"))
    assert(not is_valid("565656"))
    assert(not is_valid("824824824"))
    assert(not is_valid("2121212121"))
    print("test_is_valid: PASS")

def test():
    test_check_repeat()
    test_is_valid()

def main1(ranges):
    result = 0
    for range in ranges:
        for x in range:
            x_str = str(x)
            if check_repeat(x_str, -(len(x_str) // -2)):
                result += x
    return result

def main2(ranges):
    result = 0
    for range in ranges:
        for x in range:
            x_str = str(x)
            if not is_valid(x_str):
                result += x
    return result

def extract_range(range_str):
    min_max = [int(x) for x in range_str.split("-", 1)]
    return range(min_max[0], min_max[1])

def main(file_path):
    with open(file_path) as file:
        ranges = [extract_range(range_str) for range_str in file.read().split(",")]
    test()
    print(f"Result 1: {main1(ranges)}")
    print(f"Result 2: {main2(ranges)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", type=Path)
    args = parser.parse_args()
    main(args.file_path)

import os
import numpy

def calc_battery_joltage(bank, battery):
    joltage = 0
    factor = 1
    for i in reversed(battery):
        joltage += factor * bank[i]
        factor *= 10
    return joltage

def max_joltage_old(bank):
    assert(len(bank) > 1)
    l = 0
    r = 1
    for i in range(1, len(bank) - 1):
        if bank[i] > bank[l]:
            l = i
            r = i+1
        elif bank[i] > bank[r]:
            r = i
    if bank[-1] > bank[r]:
        r = len(bank) - 1
    return 10 * bank[l] + bank[r]

def max_joltage(bank, battery_len):
    assert(len(bank) > 1)
    assert(battery_len > 0)
    battery = [0] * battery_len
    start = 0
    end = len(bank) - battery_len + 1
    for i in range(battery_len):
        battery[i] = start + numpy.argmax(bank[start:end])
        start = battery[i] + 1
        end += 1
    return calc_battery_joltage(bank, battery)

def test():
    assert(calc_battery_joltage([8, 1, 9], [0]) == 8)
    assert(calc_battery_joltage([8, 1, 9], [1]) == 1)
    assert(calc_battery_joltage([8, 1, 9], [2]) == 9)
    assert(calc_battery_joltage([8, 1, 9], [0, 1]) == 81)
    assert(calc_battery_joltage([8, 1, 9], [0, 2]) == 89)
    assert(calc_battery_joltage([8, 1, 9], [1, 2]) == 19)
    assert(calc_battery_joltage([8, 1, 9], [0, 1, 2]) == 819)

    assert(max_joltage([9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1], 2) == 98)
    assert(max_joltage([8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], 2) == 89)
    assert(max_joltage([2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8], 2) == 78)
    assert(max_joltage([8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1], 2) == 92)
    assert(max_joltage([1, 2, 1, 2, 2, 9, 2, 3, 2, 2, 2, 2, 5, 2, 2], 2) == 95)

    assert(max_joltage([9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1], 12) == 987654321111)
    assert(max_joltage([8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], 12) == 811111111119)
    assert(max_joltage([2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8], 12) == 434234234278)
    assert(max_joltage([8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1], 12) == 888911112111)
    assert(max_joltage([1, 2, 1, 2, 2, 9, 2, 3, 2, 2, 2, 2, 5, 2, 2], 12) == 229232222522)
    print("*** Unit tests - PASSED")

def main1(banks):
    return sum([max_joltage(bank, 2) for bank in banks])

def main2(banks):
    return sum([max_joltage(bank, 12) for bank in banks])

def print_result(challenge_n, ans, exp):
    print(f"Challenge {challenge_n}. Got: {ans}. Expected: {exp}. {'PASS' if ans == exp else 'FAIL'}")

def main(file_path, exp1, exp2):
    with open(file_path) as file:
        banks = [[int(c)  for c in bank_str.rstrip()] for bank_str in file.readlines()]

    print(f"*** Input: {file_path}")
    print_result(1, main1(banks), exp1)
    print_result(2, main2(banks), exp2)

if __name__ == "__main__":
    test()
    main(os.path.dirname(__file__) + "/dummy_input.txt", 357, 3121910778619)
    main(os.path.dirname(__file__) + "/input.txt", 17109, 169347417057382)

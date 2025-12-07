import os

def main1(input):
    ans = 0
    return ans

def main2(input):
    ans = 0
    return ans

def test():
    print("*** Unit tests. PASS")

def parse_input(file_path):
    return []

def print_result(challenge_n, ans, exp):
    print(f"Challenge {challenge_n}. Got: {ans}, expected: {exp}. {'PASS' if ans == exp else 'FAIL'}")

def main(file_path, exp1, exp2):
    input = parse_input(file_path)
    print(f"*** Input: {file_path}")
    print_result(1, main1(input), exp1)
    print_result(2, main2(input), exp2)

if __name__ == "__main__":
    test()
    main(os.path.dirname(__file__) + "/dummy_input.txt", -123, -123)
    main(os.path.dirname(__file__) + "/input.txt", -123, -123)


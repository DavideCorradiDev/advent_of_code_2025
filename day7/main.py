import os
from collections import deque

def main1(input):
    beams, banks = input
    ans = 0
    for splitter_bank in banks:
        if splitter_bank:
            beams_next = [False] * len(beams)    
            for (i, on) in enumerate(beams):
                if on:
                    if i in splitter_bank:
                        beams_next[i-1] = True
                        beams_next[i+1] = True
                        ans += 1
                    else:
                        beams_next[i] = True
            beams = beams_next
            
    return ans

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_graph(beam_idx, banks, bank_idx=0, prev=None, cache=None):
    cache = cache or {}
    if (beam_idx, bank_idx) in cache:
        node = cache[(beam_idx, bank_idx)]
    else:
        node = Node(0)
        cache[(beam_idx, bank_idx)] = node
        for i, bank in enumerate(banks[bank_idx:]):
            if beam_idx in bank:
                node.left = build_graph(beam_idx-1, banks, bank_idx+i+1, prev=node, cache=cache)
                node.right = build_graph(beam_idx+1, banks, bank_idx+i+1, prev=node, cache=cache)
                break
    return node

def calculate_possibilities(node):
    if node.value > 0:
        return node.value

    if node.left and node.right:
        node.value = calculate_possibilities(node.left) + calculate_possibilities(node.right)
    else:
        node.value = 1
    
    return node.value
        
def main2(input):
    beams, banks = input
    graph = build_graph(beams.index(True), banks)
    return calculate_possibilities(graph)

def test():
    assert(calculate_possibilities(build_graph(0, [[]])) == 1)
    assert(calculate_possibilities(build_graph(1, [[1]])) == 2)
    assert(calculate_possibilities(build_graph(2, [[2],[1,3]])) == 4)
    assert(calculate_possibilities(build_graph(2, [[2],[1],[3]])) == 4)
    assert(calculate_possibilities(build_graph(2, [[2], [1, 3], [2]])) == 6)
    print("*** Unit tests. PASS")

def parse_input(file_path):
    with open(file_path) as file:
        lines = [line.rstrip() for line in file.readlines()]
        beams = [c == "S" for c in lines[0]]
        splitters = [[i for (i, x) in enumerate(line) if x == "^"] for line in lines[1:] if "^" in line]
    return (beams, splitters)

def print_result(challenge_n, ans, exp):
    print(f"Challenge {challenge_n}. Got: {ans}, expected: {exp}. {'PASS' if ans == exp else 'FAIL'}")

def main(file_path, exp1, exp2):
    input = parse_input(file_path)
    print(f"*** Input: {file_path}")
    print_result(1, main1(input), exp1)
    print_result(2, main2(input), exp2)

if __name__ == "__main__":
    test()
    main(os.path.dirname(__file__) + "/dummy_input.txt", 21, 40)
    main(os.path.dirname(__file__) + "/input.txt", 1539, 6479180385864)


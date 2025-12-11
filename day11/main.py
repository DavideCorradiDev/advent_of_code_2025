import os
from collections import deque

def count_paths_impl(graph, curr, cache):
    if curr in cache:
        return cache[curr]
    if not curr in graph:
        return 0
    count = sum([count_paths_impl(graph, next, cache) for next in graph[curr]])
    cache[curr] = count
    return count

def count_paths(graph, start, end):
    return count_paths_impl(graph, start, {end: 1})
        
def main1(graph):
    return count_paths(graph, "you", "out")

def count_valid_paths_impl(graph, curr, inter, cache):
    if curr in cache:
        return cache[curr]
    if not curr in graph:
        return (0, 0)
    count = 0
    hits = 0
    for next in graph[curr]:
        next_count, next_hits = count_valid_paths_impl(graph, next, inter, cache)
        if next_hits > hits:
            hits = next_hits
            count = next_count
        elif next_hits == hits:
            count += next_count
    if curr in inter:
        hits += 1
    cache[curr] = (count, hits)
    return (count, hits)

def count_valid_paths(graph, start, inter, end):
    count, hits = count_valid_paths_impl(graph, start, inter, {end: (1, 0)})
    return count if hits == len(inter) else 0

def main2(graph):
    return count_valid_paths(graph, "svr", ["fft", "dac"], "out")

def test():
    print("*** Unit tests. PASS")

def parse_input(file_path):
    with open(file_path) as file:
        graph = {}
        for line in file.readlines():
            node, next = line.rstrip("\n").split(": ")
            graph[node] = next.split(" ")
        return graph

def print_result(challenge_n, ans, exp):
    print(f"Challenge {challenge_n}. Got: {ans}, expected: {exp}. {'PASS' if ans == exp else 'FAIL'}")

def main(file_path, exp1, exp2):
    graph = parse_input(file_path)
    print(f"*** Input: {file_path}")
    print_result(1, main1(graph), exp1)
    print_result(2, main2(graph), exp2)

if __name__ == "__main__":
    test()
    main(os.path.dirname(__file__) + "/dummy_input_1.txt", 5, 0)
    main(os.path.dirname(__file__) + "/dummy_input_2.txt", 0, 2)
    main(os.path.dirname(__file__) + "/input.txt", 696, 473741288064360)


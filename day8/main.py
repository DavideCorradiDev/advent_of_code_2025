import os
import math

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size

    def find(self, i):
        root = self.parent[i]
        if self.parent[root] != root:
            self.parent[i] = self.find(root)
            return self.parent[i]
        return root

    def union(self, i, j):
        igroup = self.find(i)
        jgroup = self.find(j)

        if igroup == jgroup:
            return igroup

        if self.size[igroup] < self.size[jgroup]:
            self.parent[igroup] = jgroup
            self.size[jgroup] += self.size[igroup]
            return jgroup
        else:
            self.parent[jgroup] = igroup
            self.size[igroup] += self.size[jgroup]
            return igroup

def diff(p1, p2):
    return [x1 - x2 for x1, x2 in zip(p1, p2)]

def square_distance(p1, p2):
    return sum([d * d for d in diff(p1, p2)])

def main1(points, distances, connection_count):
    clusters = UnionFind(len(points))
    for c in range(connection_count):
        _, i, j = distances[c]
        clusters.union(i, j)

    return math.prod([size for size in sorted(clusters.size)[-3:]])

def main2(points, distances):
    clusters = UnionFind(len(points))
    for _, i, j in distances:
        cluster_id = clusters.union(i, j)
        if clusters.size[cluster_id] == len(points):
            return points[i][0] * points[j][0]
    return 0

def parse_input(file_path):
    with open(file_path) as file:
        return [[int(x) for x in line.rstrip("\n").split(",")] for line in file.readlines()]
    return []

def print_result(challenge_n, ans, exp):
    print(f"Challenge {challenge_n}. Got: {ans}, expected: {exp}. {'PASS' if ans == exp else 'FAIL'}")

def main(file_path, params1, exp2):
    print(f"*** Input: {file_path}")

    points = parse_input(file_path)
    distances = []
    for i in range(len(points) - 1):
        for j in range(i+1, len(points)):
            distances.append((square_distance(points[i], points[j]), i, j))
    distances = sorted(distances)

    connection_count1, exp1 = params1
    print_result(1, main1(points, distances, connection_count1), exp1)
    
    print_result(2, main2(points, distances), exp2)

if __name__ == "__main__":
    main(os.path.dirname(__file__) + "/dummy_input.txt", (10, 40), 25272)
    main(os.path.dirname(__file__) + "/input.txt", (1000, 84968), 8663467782)


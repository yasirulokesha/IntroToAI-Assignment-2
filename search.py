import sys
import heapq
import re

class Graph:
    def __init__(self):
        self.nodes = {}  # Store coordinates {node: (x, y)}
        self.edges = {}  # Adjacency list {node: [(neighbor, cost), ...]}
        self.origin = None
        self.destinations = set()

    def add_node(self, node, x, y):
        self.nodes[node] = (x, y)
        self.edges[node] = []

    def add_edge(self, start, end, cost):
        self.edges[start].append((end, cost))

    def parse_file(self, filename):
        with open(PathFinder-test.txt, 'r') as f:
            lines = f.readlines()

        section = None
        for line in lines:
            line = line.strip()
            if not line:
                continue

            if line.startswith("Nodes:"):
                section = "nodes"
                continue
            elif line.startswith("Edges:"):
                section = "edges"
                continue
            elif line.startswith("Origin:"):
                section = "origin"
                continue
            elif line.startswith("Destinations:"):
                section = "destinations"
                continue

            if section == "nodes":
                match = re.match(r"(\d+): \((\d+),(\d+)\)", line)
                if match:
                    node, x, y = map(int, match.groups())
                    self.add_node(node, x, y)

            elif section == "edges":
                match = re.match(r"\((\d+),(\d+)\): (\d+)", line)
                if match:
                    start, end, cost = map(int, match.groups())
                    self.add_edge(start, end, cost)

            elif section == "origin":
                self.origin = int(line)

            elif section == "destinations":
                self.destinations = set(map(int, line.split(";")))

    def __str__(self):
        return f"Nodes: {self.nodes}\nEdges: {self.edges}\nOrigin: {self.origin}\nDestinations: {self.destinations}"


# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.parse_file("input.txt")  # Replace with actual file name
    print(graph)

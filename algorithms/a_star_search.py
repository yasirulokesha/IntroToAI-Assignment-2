import sys
import heapq
import math
from graph import Graph
from read_file import read_file  # Import function to parse input files

def euclidean_distance(node1, node2, graph):
    """Computes Euclidean distance between two nodes."""
    x1, y1 = graph.nodes[node1]
    x2, y2 = graph.nodes[node2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def a_star(problem):
    """Performs A* Search with tie-breaking rules."""
    graph = problem.graph
    start = problem.origin
    goals = problem.destinations

    # Priority queue: (f, g, node, path)
    priority_queue = [(0, 0, start, [start])]  # (f, g, node, path)
    visited = {}

    while priority_queue:
        f, g, node, path = heapq.heappop(priority_queue)  # Expand lowest-cost node

        if node in goals:
            return path, g  # Goal reached, return path and cost

        if node not in visited or g < visited[node]:
            visited[node] = g  # Store the best known cost

            # Get neighbors, sort them in ascending order
            neighbors = sorted(graph.edges[node], key=lambda x: x[0])  # Sort by node ID
            for neighbor, edge_cost in neighbors:
                new_g = g + edge_cost  # Actual cost
                h = min(euclidean_distance(neighbor, goal, graph) for goal in goals)  # Heuristic
                f = new_g + h  # Total cost

                heapq.heappush(priority_queue, (f, new_g, neighbor, path + [neighbor]))

    return None, float("inf")  # No path found
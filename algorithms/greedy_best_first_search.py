import sys
import heapq
import math

def euclidean_distance(node1, node2, graph):
    """Computes Euclidean distance between two nodes."""
    x1, y1 = graph.nodes[node1]
    x2, y2 = graph.nodes[node2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def gbfs(problem):
    """Performs Greedy Best-First Search (GBFS) with tie-breaking rules."""
    graph = problem.graph
    start = problem.origin
    goals = problem.destinations

    # Priority queue: (h, node, path)
    priority_queue = [(0, start, [start])]  # (h, node, path)
    visited = set()

    while priority_queue:
        h, node, path = heapq.heappop(priority_queue)  # Expand lowest heuristic value

        if node in goals:
            return path, len(path)  # Goal reached, return path and number of nodes visited

        if node not in visited:
            visited.add(node)

            # Get neighbors, sort them in ascending order
            neighbors = sorted(graph.edges[node], key=lambda x: x[0])  # Sort by node ID
            for neighbor, edge_cost in neighbors:
                if neighbor not in visited:
                    h_new = min(euclidean_distance(neighbor, goal, graph) for goal in goals)  # Heuristic
                    heapq.heappush(priority_queue, (h_new, neighbor, path + [neighbor]))

    return None, float("inf")  # No path found
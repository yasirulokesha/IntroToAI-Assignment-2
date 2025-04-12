import sys
import heapq
from graph import Graph

def cus1(problem):
    """Performs Uniform Cost Search (UCS) with tie-breaking rules."""
    graph = problem.graph
    start = problem.origin
    goals = problem.destinations

    # Priority queue: (cost, node, path)
    priority_queue = [(0, start, [start])]  # (cost, node, path)
    visited = {}

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)  # Expand lowest-cost node

        if node in goals:
            return path, node  # Goal reached, return path and cost

        if node not in visited or cost < visited[node]:
            visited[node] = cost  # Store the best known cost

            # Get neighbors, sort them in ascending order before adding to queue
            neighbors = sorted(graph.edges[node], key=lambda x: x[0])  # Sort by node ID
            for neighbor, edge_cost in neighbors:
                new_cost = cost + edge_cost  # Total cost so far
                heapq.heappush(priority_queue, (new_cost, neighbor, path + [neighbor]))

    return None, float("inf")  # No path found
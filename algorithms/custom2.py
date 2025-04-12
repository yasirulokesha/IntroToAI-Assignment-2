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

def bi_directional_a_star(problem):
    """Performs Bi-Directional A* Search with tie-breaking rules."""
    graph = problem.graph
    start = problem.origin
    goals = problem.destinations

    # Choose the closest goal as the search target
    target = min(goals, key=lambda goal: euclidean_distance(start, goal, graph))

    # Priority queues for forward and backward search: (f, g, node, path)
    forward_queue = [(0, 0, start, [start])]
    backward_queue = [(0, 0, target, [target])]

    # Visited nodes with best costs
    forward_visited = {}
    backward_visited = {}

    while forward_queue and backward_queue:
        # Forward search step
        f_f, g_f, node_f, path_f = heapq.heappop(forward_queue)
        if node_f in backward_visited:
            return path_f + backward_visited[node_f][::-1][1:], g_f  # Merge paths

        if node_f not in forward_visited or g_f < forward_visited[node_f]:
            forward_visited[node_f] = path_f
            neighbors = sorted(graph.edges[node_f], key=lambda x: x[0])  # Sort nodes
            for neighbor, edge_cost in neighbors:
                new_g = g_f + edge_cost
                h = euclidean_distance(neighbor, target, graph)
                f = new_g + h
                heapq.heappush(forward_queue, (f, new_g, neighbor, path_f + [neighbor]))

        # Backward search step
        f_b, g_b, node_b, path_b = heapq.heappop(backward_queue)
        if node_b in forward_visited:
            return forward_visited[node_b] + path_b[::-1][1:], g_b  # Merge paths

        if node_b not in backward_visited or g_b < backward_visited[node_b]:
            backward_visited[node_b] = path_b
            neighbors = sorted(graph.edges[node_b], key=lambda x: x[0])  # Sort nodes
            for neighbor, edge_cost in neighbors:
                new_g = g_b + edge_cost
                h = euclidean_distance(neighbor, start, graph)
                f = new_g + h
                heapq.heappush(backward_queue, (f, new_g, neighbor, path_b + [neighbor]))

    return None, float("inf")  # No path found
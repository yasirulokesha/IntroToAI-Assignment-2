import heapq

# Performs Greedy Best-First Search (GBFS) with tie-breaking rules.
def gbfs(problem):
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
                    h_new = min( graph.nodes[neighbor].distance_to(graph.nodes[goal]) for goal in goals)  # Heuristic
                    heapq.heappush(priority_queue, (h_new, neighbor, path + [neighbor]))

    return None, float("inf")  # No path found
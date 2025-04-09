from collections import deque

# Performs Breadth-First Search (BFS) with tie-breaking rules.
def bfs(problem):
    graph = problem.graph
    start = problem.origin
    goals = problem.destinations

    queue = deque([(start, [start], 0)])  # (current_node, path, cost)
    visited = set()

    while queue:
        node, path, cost = queue.popleft()  # FIFO order (Breadth-First)

        if node in goals:
            return path, node  # Found a goal, return the path and cost

        if node not in visited:
            visited.add(node)

            # Get neighbors, sort them in ascending order before adding to queue
            neighbors = sorted(graph.edges[node], key=lambda x: x[0])  # Sort by node ID
            for neighbor, edge_cost in neighbors:  # FIFO order for BFS
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor], cost + edge_cost))

    return None, float("inf")  # No path found
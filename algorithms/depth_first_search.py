import sys

def dfs(problem):
    """Performs Depth-First Search (DFS) with tie-breaking rules."""
    graph = problem.graph
    start = problem.origin
    goals = problem.destinations

    stack = [(start, [start], 0)]  # (current_node, path, cost)
    visited = set()

    while stack:
        node, path, cost = stack.pop()  # LIFO order (Depth-First)

        if node in goals:
            return path, cost  # Found a goal, return the path and cost

        if node not in visited:
            visited.add(node)
            
            # Get neighbors, sort them in ascending order before adding to stack
            neighbors = sorted(graph.edges[node], key=lambda x: x[0])  # Sort by node ID
            
            for neighbor, edge_cost in reversed(neighbors):  # Reverse to maintain DFS LIFO order
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor], cost + edge_cost))

    return None, float("inf")  # No path found

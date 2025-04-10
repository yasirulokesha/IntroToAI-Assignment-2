import sys

# Performs Depth-First Search (DFS) with tie-breaking rules.
def dfs(problem):
    graph = problem.graph
    start = problem.origin
    goals = problem.destinations
    
    # Convert types to string for consistent comparison
    start_str = str(start)
    goals_str = {str(goal) for goal in goals}
    
    # Check if the start node is already a goal
    if start_str in goals_str:
        return [start], start  # Return path and the goal node found

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

def dfs(problem):
    graph = problem.graph
    start = problem.origin
    goals = problem.destinations
    
    # Convert types to string for consistent comparison
    start_str = str(start)
    goals_str = {str(goal) for goal in goals}
    
    # Check if the start node is already a goal
    if start_str in goals_str:
        for goal in goals:
            if str(goal) == start_str:
                return [start], goal

    stack = [(start, [start])]  # (current_node, path)
    visited = set()

    while stack:
        node, path = stack.pop()  # LIFO order (Depth-First)
        
        # Check if current node is a goal
        node_str = str(node)
        if node_str in goals_str:
            for goal in goals:
                if str(goal) == node_str:
                    return path, goal

        if node not in visited:
            visited.add(node)
            
            # Get neighbors, sort them in ascending order before adding to stack
            neighbors = sorted(graph.edges[node], key=lambda x: x[0])  # Sort by node ID
            
            for neighbor, _ in reversed(neighbors):  # Reverse to maintain DFS LIFO order
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None, None  # No path found
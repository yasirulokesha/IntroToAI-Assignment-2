import heapq

# Performs A* Search with tie-breaking rules.
def a_star(problem):
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
    
    # Use a counter for tie-breaking when f-values are equal
    counter = 0
    
    # Priority queue: (f, tiebreaker, g, node, path)
    # The tiebreaker ensures consistent ordering when f-values are identical
    priority_queue = [(0, counter, 0, start, [start])]
    visited = set()  # Track visited nodes to avoid cycles
    cost_so_far = {start: 0}  # Keep track of the cheapest path to each node
    
    while priority_queue:
        f, _, g, node, path = heapq.heappop(priority_queue)
        
        # Convert node for comparison with goals
        node_str = str(node)
        
        if node_str in goals_str:
            for goal in goals:
                if str(goal) == node_str:
                    return path, goal
        
        # Skip if we've already processed this node with a better or equal path
        if node in visited and g >= cost_so_far[node]:
            continue
            
        visited.add(node)
        cost_so_far[node] = g
        
        # Get neighbors, sort them in ascending order for deterministic behavior
        neighbors = sorted(graph.edges[node], key=lambda x: x[0])
        
        for neighbor, edge_cost in neighbors:
            # Skip already visited nodes with better paths
            if neighbor in visited and g + edge_cost >= cost_so_far.get(neighbor, float('inf')):
                continue
                
            new_g = g + edge_cost
            
            # Calculate heuristic for all goals and take the minimum
            h = min(
                graph.nodes[neighbor].distance_to(graph.nodes[goal]) 
                for goal in goals
            )
            
            new_f = new_g + h
            
            # Increment counter for tie-breaking
            counter += 1
            
            heapq.heappush(priority_queue, (new_f, counter, new_g, neighbor, path + [neighbor]))
    
    return None, None  # No path found

# Uninformed - Dijkstra's Algorithm
    
import heapq

def custom_search_1(problem):
    
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
    
    # Priority queue: (cost, tiebreaker, node, path)
    counter = 0
    priority_queue = [(0, counter, start, [start])]
    visited = {}  # node -> best cost so far
    
    while priority_queue:
        cost, _, node, path = heapq.heappop(priority_queue)
        
        # Check if we've found a goal
        node_str = str(node)
        if node_str in goals_str:
            for goal in goals:
                if str(goal) == node_str:
                    return path, goal
        
        # Skip if we've already found a better path to this node
        if node in visited and cost >= visited[node]:
            continue
            
        visited[node] = cost
        
        # Get neighbors, sort them for deterministic behavior
        neighbors = sorted(graph.edges[node], key=lambda x: x[0])
        
        for neighbor, edge_cost in neighbors:
            new_cost = cost + edge_cost
            
            # Only consider this path if it's better than any previously found
            if neighbor not in visited or new_cost < visited.get(neighbor, float('inf')):
                # Increment counter for tie-breaking
                counter += 1
                heapq.heappush(priority_queue, (new_cost, counter, neighbor, path + [neighbor]))
    
    return None, None  # No path found
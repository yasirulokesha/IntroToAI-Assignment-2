from collections import deque
from ..graph import Node

def gbfs_fun(graph):
    """
    Greedy Best-First Search algorithm.
    Uses heuristic (Euclidean distance to nearest destination) to guide search.
    
    Returns:
        (goal_node, num_nodes_created, path)
    """
    # Initialize
    start_node = Node(graph.origin)
    if graph.is_destination(start_node.state):
        return start_node.state, 1, start_node.get_path()
    
    # Calculate heuristic for start node
    start_node.f_value = min(graph.euclidean_distance(start_node.state, dest) 
                             for dest in graph.destinations)
    
    # Use a priority queue for GBFS
    frontier = [start_node]
    visited = set()
    nodes_created = 1
    
    while frontier:
        # Get the node with lowest heuristic value
        current = heapq.heappop(frontier)
        
        # Skip if already visited
        if current.state in visited:
            continue
        
        # Mark as visited
        visited.add(current.state)
        
        # Get neighbors, sorted in ascending order
        neighbors = graph.get_neighbors(current.state)
        
        # Add neighbors to priority queue
        for neighbor in neighbors:
            if neighbor not in visited:
                # Get edge cost
                edge_cost = graph.get_edge_cost(current.state, neighbor)
                # Create new node
                new_node = Node(
                    state=neighbor,
                    parent=current,
                    action=f"{current.state}->{neighbor}",
                    path_cost=current.path_cost + edge_cost
                )
                nodes_created += 1
                
                # Check if this is a destination
                if graph.is_destination(neighbor):
                    return neighbor, nodes_created, new_node.get_path()
                
                # Calculate heuristic (minimum distance to any destination)
                new_node.f_value = min(graph.euclidean_distance(neighbor, dest) 
                                       for dest in graph.destinations)
                
                # Add to priority queue
                heapq.heappush(frontier, new_node)
    
    # No solution found
    return None, nodes_created, []
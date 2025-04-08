from collections import deque
from ..graph import Node

def a_star(graph):
    """
    A* Search algorithm.
    Uses path cost plus heuristic to guide search.
    
    Returns:
        (goal_node, num_nodes_created, path)
    """
    # Initialize
    start_node = Node(graph.origin)
    if graph.is_destination(start_node.state):
        return start_node.state, 1, start_node.get_path()
    
    # Calculate f-value (g + h) for start node
    # g = path cost so far (0 for start)
    # h = heuristic (minimum distance to any destination)
    start_node.f_value = start_node.path_cost + min(
        graph.euclidean_distance(start_node.state, dest) for dest in graph.destinations
    )
    
    # Use a priority queue for A*
    frontier = [start_node]
    # Use a dictionary to track best costs to each node
    best_cost = {graph.origin: 0}
    nodes_created = 1
    
    while frontier:
        # Get the node with lowest f-value
        current = heapq.heappop(frontier)
        
        # Check if this is a destination
        if graph.is_destination(current.state):
            return current.state, nodes_created, current.get_path()
        
        # Get neighbors, sorted in ascending order
        neighbors = graph.get_neighbors(current.state)
        
        # Add neighbors to priority queue
        for neighbor in neighbors:
            # Get edge cost
            edge_cost = graph.get_edge_cost(current.state, neighbor)
            # Calculate new path cost
            new_cost = current.path_cost + edge_cost
            
            # Check if we found a better path to this neighbor
            if neighbor not in best_cost or new_cost < best_cost[neighbor]:
                # Update best cost
                best_cost[neighbor] = new_cost
                
                # Create new node
                new_node = Node(
                    state=neighbor,
                    parent=current,
                    action=f"{current.state}->{neighbor}",
                    path_cost=new_cost
                )
                nodes_created += 1
                
                # Calculate f-value (g + h)
                new_node.f_value = new_cost + min(
                    graph.euclidean_distance(neighbor, dest) for dest in graph.destinations
                )
                
                # Add to priority queue
                heapq.heappush(frontier, new_node)
    
    # No solution found
    return None, nodes_created, []
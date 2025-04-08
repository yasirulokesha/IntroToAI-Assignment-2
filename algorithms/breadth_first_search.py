from collections import deque
from ..graph import Node

def bfs_fun(graph):
    """
    Breadth-First Search algorithm.
    
    Returns:
        (goal_node, num_nodes_created, path)
    """
    # Initialize
    start_node = Node(graph.origin)
    if graph.is_destination(start_node.state):
        return start_node.state, 1, start_node.get_path()
    
    # Use a queue for BFS
    queue = deque([start_node])
    visited = set([graph.origin])
    nodes_created = 1
    
    while queue:
        # Get the first node in the queue (FIFO)
        current = queue.popleft()
        
        # Get neighbors, sorted in ascending order
        neighbors = graph.get_neighbors(current.state)
        
        # Add neighbors to queue
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
                
                # Mark as visited and add to queue
                visited.add(neighbor)
                queue.append(new_node)
    
    # No solution found
    return None, nodes_created, []
from collections import deque
import heapq
from graph import Node

def dfs(graph):
    """
    Depth-First Search algorithm.
    
    Returns:
        (goal_node, num_nodes_created, path)
    """
    # Initialize
    start_node = Node(graph.origin)
    if graph.is_destination(start_node.state):
        return start_node.state, 1, start_node.get_path()
    
    # Use a stack for DFS
    stack = [start_node]
    visited = set()
    nodes_created = 1
    
    while stack:
        # Get the last node in the stack (LIFO)
        current = stack.pop()
        
        # Skip if already visited
        if current.state in visited:
            continue
        
        # Mark as visited
        visited.add(current.state)
        
        # Get neighbors, sorted in ascending order
        neighbors = graph.get_neighbors(current.state)
        
        # Add neighbors to stack (in reverse order so smallest is popped first)
        for neighbor in reversed(neighbors):
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
                
                # Add to stack
                stack.append(new_node)
    
    # No solution found
    return None, nodes_created, []


def bfs(graph):
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


def gbfs(graph):
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


def cus1(graph):
    """
    Custom Search 1: Uniform Cost Search (Dijkstra's Algorithm)
    An uninformed search strategy that finds the lowest-cost path.
    
    Returns:
        (goal_node, num_nodes_created, path)
    """
    # Initialize
    start_node = Node(graph.origin)
    if graph.is_destination(start_node.state):
        return start_node.state, 1, start_node.get_path()
    
    # Set f_value to path cost for uniform cost search
    start_node.f_value = start_node.path_cost
    
    # Use a priority queue
    frontier = [start_node]
    # Track visited nodes and their costs
    visited = {}  # node_id -> cost
    nodes_created = 1
    
    while frontier:
        # Get the node with lowest path cost
        current = heapq.heappop(frontier)
        
        # If we've already found a better path to this node, skip it
        if current.state in visited and visited[current.state] <= current.path_cost:
            continue
        
        # Mark as visited with current cost
        visited[current.state] = current.path_cost
        
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
            if neighbor not in visited or new_cost < visited[neighbor]:
                # Create new node
                new_node = Node(
                    state=neighbor,
                    parent=current,
                    action=f"{current.state}->{neighbor}",
                    path_cost=new_cost
                )
                nodes_created += 1
                
                # Set f_value to path cost for uniform cost search
                new_node.f_value = new_cost
                
                # Add to priority queue
                heapq.heappush(frontier, new_node)
    
    # No solution found
    return None, nodes_created, []


def cus2(graph):
    """
    Custom Search 2: Bidirectional A* Search
    An informed search that searches simultaneously from the start and goal nodes.
    Since there may be multiple goals, we'll choose the closest one by heuristic.
    
    Returns:
        (goal_node, num_nodes_created, path)
    """
    # We need to select one destination for bidirectional search
    # Choose the destination with the smallest heuristic value from origin
    closest_dest = min(
        graph.destinations,
        key=lambda dest: graph.euclidean_distance(graph.origin, dest)
    )
    
    # Initialize forward search from origin
    start_node = Node(graph.origin)
    start_node.f_value = graph.euclidean_distance(graph.origin, closest_dest)
    
    # Initialize backward search from destination
    goal_node = Node(closest_dest)
    goal_node.f_value = graph.euclidean_distance(closest_dest, graph.origin)
    
    # If start is goal, return immediately
    if graph.origin == closest_dest:
        return graph.origin, 1, [graph.origin]
    
    # Set up forward search
    forward_frontier = [start_node]
    forward_reached = {graph.origin: start_node}
    
    # Set up backward search
    backward_frontier = [goal_node]
    backward_reached = {closest_dest: goal_node}
    
    # Count nodes created
    nodes_created = 2
    
    # Track best path found so far
    best_path_cost = float('inf')
    best_path_node = None
    middle_node = None
    
    while forward_frontier and backward_frontier:
        # Check if we should terminate
        if min(node.f_value for node in forward_frontier) + \
           min(node.f_value for node in backward_frontier) >= best_path_cost:
            break
        
        # Forward search step
        current = heapq.heappop(forward_frontier)
        
        # Check for intersection with backward search
        if current.state in backward_reached:
            # Found a path through current node
            backward_node = backward_reached[current.state]
            path_cost = current.path_cost + backward_node.path_cost
            
            if path_cost < best_path_cost:
                best_path_cost = path_cost
                middle_node = current.state
                best_path_node = (current, backward_node)
        
        # Expand forward search
        for neighbor in graph.get_neighbors(current.state):
            edge_cost = graph.get_edge_cost(current.state, neighbor)
            new_cost = current.path_cost + edge_cost
            
            if neighbor not in forward_reached or new_cost < forward_reached[neighbor].path_cost:
                new_node = Node(
                    state=neighbor,
                    parent=current,
                    action=f"{current.state}->{neighbor}",
                    path_cost=new_cost
                )
                nodes_created += 1
                
                # A* uses g + h
                new_node.f_value = new_cost + graph.euclidean_distance(neighbor, closest_dest)
                
                forward_reached[neighbor] = new_node
                heapq.heappush(forward_frontier, new_node)
        
        # Backward search step
        if not backward_frontier:
            break
            
        current = heapq.heappop(backward_frontier)
        
        # Check for intersection with forward search
        if current.state in forward_reached:
            # Found a path through current node
            forward_node = forward_reached[current.state]
            path_cost = forward_node.path_cost + current.path_cost
            
            if path_cost < best_path_cost:
                best_path_cost = path_cost
                middle_node = current.state
                best_path_node = (forward_node, current)
        
        # Backward search is trickier since edges are directional
        # We need to find all nodes that can reach the current node
        for node_id in graph.nodes:
            if (node_id, current.state) in graph.edges:
                edge_cost = graph.get_edge_cost(node_id, current.state)
                new_cost = current.path_cost + edge_cost
                
                if node_id not in backward_reached or new_cost < backward_reached[node_id].path_cost:
                    new_node = Node(
                        state=node_id,
                        parent=current,
                        action=f"{node_id}->{current.state}",
                        path_cost=new_cost
                    )
                    nodes_created += 1
                    
                    # A* uses g + h
                    new_node.f_value = new_cost + graph.euclidean_distance(node_id, graph.origin)
                    
                    backward_reached[node_id] = new_node
                    heapq.heappush(backward_frontier, new_node)
    
    # Construct path if solution found
    if best_path_node:
        forward_path = best_path_node[0].get_path()
        backward_path = best_path_node[1].get_path()[1:]  # Skip the duplicate middle node
        backward_path.reverse()
        complete_path = forward_path + backward_path
        return closest_dest, nodes_created, complete_path
    
    # Check if any of the original destinations were found in the forward search
    for dest in graph.destinations:
        if dest in forward_reached:
            return dest, nodes_created, forward_reached[dest].get_path()
    
    # No solution found
    return None, nodes_created, []
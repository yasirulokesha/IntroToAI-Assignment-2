# from collections import deque
from ..graph import Node, Graph

# # Depth-First Search algorithm.
# def dfs_fun(graph):
#     # Initialize
#     start_node = Node(graph.origin)
#     if graph.is_destination(start_node.state):
#         return start_node.state, 1, start_node.get_path()
    
#     # Use a stack for DFS
#     stack = [start_node]
#     visited = set()
#     nodes_created = 1
    
#     while stack:
#         # Get the last node in the stack (LIFO)
#         current = stack.pop()
        
#         # Skip if already visited
#         if current.state in visited:
#             continue
        
#         # Mark as visited
#         visited.add(current.state)
        
#         # Get neighbors, sorted in ascending order
#         neighbors = graph.get_neighbors(current.state)
        
#         # Add neighbors to stack (in reverse order so smallest is popped first)
#         for neighbor in reversed(neighbors):
#             if neighbor not in visited:
#                 # Get edge cost
#                 edge_cost = graph.get_edge_cost(current.state, neighbor)
#                 # Create new node
#                 new_node = Node(
#                     state=neighbor,
#                     parent=current,
#                     action=f"{current.state}->{neighbor}",
#                     path_cost=current.path_cost + edge_cost
#                 )
#                 nodes_created += 1
                
#                 # Check if this is a destination
#                 if graph.is_destination(neighbor):
#                     return neighbor, nodes_created, new_node.get_path()
                
#                 # Add to stack
#                 stack.append(new_node)
    
#     # No solution found
#     return None, nodes_created, []


import sys

def dfs_fun(problem):
    """Performs Depth-First Search (DFS) on the graph."""
    graph = problem.graph
    start = problem.origin
    goals = problem.destinations
    
    result_graph = Graph()

    stack = [(start, [start], 0)]  # (current_node, path, cost)
    visited = set()

    while stack:
        node, path, cost = stack.pop()  # LIFO order (Depth-First)

        if node in goals:
            return path, cost  # Found a goal, return the path and cost

        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in sorted(graph.edges[node], reverse=True):  
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor], cost + edge_cost))

    return None, float("inf")  # No path found

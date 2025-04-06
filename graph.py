import math

class Node:
    # Represents a node in the graph with coordinates
    def __init__(self, state, action, parent, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.action = action
        self.state = state
        self.parent = parent
    
    # Distance to another node
    def distance_to(self, other_node):
        return math.sqrt((self.x - other_node.x)**2 + (self.y - other_node.y)**2)

class Graph:
    # Represents the graph with nodes and edges
    def __init__(self):
        self.nodes = {}  
        self.edges = {} 
    
    # Add a node to the graph
    def add_node(self, node_id, x, y):
        self.nodes[node_id] = Node(node_id, x, y)
        if node_id not in self.edges:
            self.edges[node_id] = []
    
    # Add a directed edge to the graph
    def add_edge(self, from_node, to_node, cost):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, cost))
    
    # Get neighbors of a node, sorted by node ID
    def get_neighbors(self, node_id):
        if node_id in self.edges:
            # Sort neighbors by node ID in ascending order
            return sorted(self.edges[node_id], key=lambda x: x[0])
        return []
    
    # Get the cost of an edge
    def get_edge_cost(self, from_node, to_node):
        for neighbor, cost in self.edges.get(from_node, []):
            if neighbor == to_node:
                return cost
        # Return infinity if there's no direct edge
        return float('inf')  
import math

class Node:
    # Represents a node in the graph with coordinates
    def __init__(self, id, x, y, state=None, parent=None):
        self.id = id
        self.x = x
        self.y = y
        self.state = state
        self.parent = parent
    
    # Distance to another node
    def distance_to(self, other_node):
        return math.sqrt((self.x - other_node.x)**2 + (self.y - other_node.y)**2)

class Graph:
    # Create a graph with nodes and edges
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
    
    # Print the graph (NODES + EDGES)
    def print_graph(self):
        print("Nodes:")
        for node_id, node in self.nodes.items():
            print(f"  Node {node_id}: ({node.x}, {node.y})")
        
        print("\nEdges:")
        for from_node, neighbors in self.edges.items():
            for (to_node, cost) in neighbors:
                print(f"  {from_node} -> {to_node} (Cost: {cost})")

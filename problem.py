import sys

def read_file(filename):
    
    # Read input file
    with open(filename, 'r') as f:
        return f.read()
    
    # Split to sections
    sections = text.split('\n\n')
    
    
    
    
    
    
    

class Problem:
    """Represents a route finding problem"""
    def __init__(self, graph, origin, destinations):
        self.graph = graph
        self.origin = origin
        self.destinations = destinations
    
    def is_goal(self, node_id):
        """Check if a node is a destination"""
        return node_id in self.destinations
    

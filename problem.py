from collections import defaultdict
import re
import sys

# Represents a route finding problem
class Problem:
    def __init__(self, graph, origin, destinations):
        self.graph = graph
        self.origin = origin
        self.destinations = destinations
       
    # Check if a node is a destination
    def is_goal(self, node_id):
        return node_id in self.destinations
    
    
# Read the file and make a Problem class to proceed
def read_file(filename):
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # Parse main sections
    sections = {}
    section_names = ["Nodes:", "Edges:", "Origin:", "Destinations:"]
    current_section = None
    section_content = []
    
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if line in section_names:
            if current_section:
                sections[current_section] = '\n'.join(section_content)
            current_section = line
            section_content = []
        elif current_section:
            section_content.append(line)
    
    # Add the last section
    if current_section and section_content:
        sections[current_section] = '\n'.join(section_content)
    
    # Extract nodes
    nodes = set()
    if "Nodes:" in sections:
        node_lines = sections["Nodes:"].split('\n')
        for line in node_lines:
            if ":" in line:
                node_id = line.split(":")[0].strip()
                nodes.add(node_id)
    
    # Extract edges
    # Edges are dicts that have the node id as key, and a list of connected nodes as value eg {'1' : ['2', '3']}
    edges = defaultdict(list)
    if "Edges:" in sections:
        edge_lines = sections["Edges:"].split('\n')
        for line in edge_lines:
            match = re.match(r'^\((\d+),(\d+)\):\s*\d+$', line)
            if match:
                a, b = match.group(1), match.group(2)
                # treat edges as undirected
                if b not in edges[a]:
                    edges[a].append(b)
                if a not in edges[b]:
                    edges[b].append(a)
    
    # Sort edges for tie-breaking
    for node in edges:
        edges[node] = sorted(edges[node], key=lambda x: int(x))
    
    # Extract origin
    origin = None
    if "Origin:" in sections:
        origin_text = sections["Origin:"].strip()
        if origin_text:
            origin = origin_text
    
    # Extract destinations
    destinations = set()
    if "Destinations:" in sections:
        dest_text = sections["Destinations:"].strip()
        if dest_text:
            # Split by semicolon
            for part in dest_text.split(';'):
                part = part.strip()
                if part:
                    # Take only the first word in case there are comments
                    dest = part.split()[0].strip()
                    destinations.add(dest)
                    
    print("nodes: " + str(nodes))
    print("Edges: " + str(edges))
    print("Origin: " + str(origin))
    print("Destination: " + str(destinations))
    
    return Problem(graph, origin, destinations)
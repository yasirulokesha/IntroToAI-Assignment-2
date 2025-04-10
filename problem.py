from collections import defaultdict
import re
import sys
from graph import Node, Graph

# Represents a route finding problem
class Problem:
    def __init__(self, graph, origin, destinations):
        self.graph = graph
        self.origin = origin
        self.destinations = destinations

# Read the file and make a Problem class to proceed
def read_file(filename):
    
    with open(filename, 'r') as f:
        content = f.read()
        
    
    # Parse main sections
    sections = {}
    section_names = ["Nodes:", "Edges:", "Origin:", "Destinations:"]
    current_section = None
    section_content = []
    
    # Make a graph for the problem
    problem_graph = Graph()
    
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
        
        
    # Check if all required sections are present, print error if missing
    for section in section_names:
        if section not in sections:
            print(f"ERROR: Missing {section} section in the input file.")
            sys.exit(1)  # Exit if required section is missing
    
    # Extract nodes
    if "Nodes:" in sections:
        node_lines = sections["Nodes:"].split('\n')
        for line in node_lines:
            if ":" in line:
                node_id = line.split(":")[0].strip()
                node_x, node_y = line.split(":")[1].strip().strip("()").split(",")
                problem_graph.add_node(node_id, int(node_x), int(node_y))
    
    # Extract edges
    # Edges are dicts that have the node id as key, and a list of connected nodes as value eg {'1' : ['2', '3']}
    if "Edges:" in sections:
        edge_lines = sections["Edges:"].split('\n')
        for line in edge_lines:
            line = line.strip("()").split(",")
            node_from, node_to = line[0], line[1].split(":")[0].strip("()")
            cost = int(line[1].split(":")[1].strip())
            problem_graph.add_edge(node_from, node_to, cost)
            
    # Extract origin
    origin = None
    if "Origin:" in sections:
        origin_text = sections["Origin:"].strip()
        if origin_text:
             # Check if there is more than one origin
            origin_list = origin_text.split(';')
            if len(origin_list) > 1:
                print("ERROR: Multiple origins specified. There must be exactly one origin.")
                sys.exit(1)  # Exit if there are multiple origins
            origin = origin_list[0].strip()
            
    if not origin:
        print("ERROR: Missing or invalid origin.")
        sys.exit(1)
    
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

    return Problem(problem_graph, origin, destinations)
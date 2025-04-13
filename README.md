# Tree-Based Search Algorithms for Route Finding

## Introduction

This project is an implementation of various tree-based search algorithms to solve the Route Finding Problem. The goal is to find optimal paths from an origin node to destination nodes in a 2D graph using both informed and uninformed search methods.

## Features

Implemented search algorithms:

- Depth-First Search (DFS)

- Breadth-First Search (BFS)

- Greedy Best-First Search (GBFS)

- A*Search (A*)

- Custom Uninformed Search (CUS1 - Uniformed Cost Search)

- Custom Informed Search (CUS2 - Bi-Directional A* Search )

Reads graph data from structured text files

Supports batch testing via the command line

## Getting Started
### Prerequisites
- Python 3.8 or higher
- Graph data in the format of a text file with the following structure:
```
- Nodes: are defined with their coordinates `(x, y)`
- Edges: are directional and include traversal costs
- Origin: defines the starting node
- Destinations: defines one or more goal nodes (separated by `;`)
```# Tree-Based Search Algorithms for Route Finding

## Introduction

This project is an implementation of various tree-based search algorithms to solve the Route Finding Problem. The goal is to find optimal paths from an origin node to destination nodes in a 2D graph using both informed and uninformed search methods.

## Features

Implemented search algorithms:

- Depth-First Search (DFS)

- Breadth-First Search (BFS)

- Greedy Best-First Search (GBFS)

- A*Search (A*)

- Custom Uninformed Search (CUS1 - Uniformed Cost Search)

- Custom Informed Search (CUS2 - Bi-Directional A* Search )

Reads graph data from structured text files

Supports batch testing via the command line

## Getting Started
### Prerequisites
- Python 3.8 or higher
- Graph data in the format of a text file with the following structure:
```
- Nodes: are defined with their coordinates `(x, y)`
- Edges: are directional and include traversal costs
- Origin: defines the starting node
- Destinations: defines one or more goal nodes (separated by `;`)
```

## File Format

The input files should follow this format:

```
Nodes:
1: (4,1)
2: (2,2)
...

Edges:
(2,1): 4
(3,1): 5
...

Origin:
2

Destinations:
5; 4
  
```
  
## Installation

### Clone this repository:
```
git clone https://github.com/](https://github.com/yasirulokesha/IntroToAI-Assignment-2.git
```

## Usage

Run the program using the following command:

```
python search.py <filename> <method>
```

Where:

`<filename>` is the path to the input file

`<method>` is one of DFS, BFS, GBFS, A*, CUS1, or CUS2

## Example
Executable file is provided in the repository. You can run it from the terminal using the following command:
```
python search.py <filename> <method>
```

Output Format
```
<filename> <method>
<goal> 
<number_of_nodes>
<path>
```
Example:
```
Searching the path using Custom 2 (Recursive Best First Search) Search...
PathFinder-test.txt CUS2

********* Search Results *********
Found Goal:      None
Node Visited:    1
Path:            4

```

## Testing

There has 10 test cases have been created to cover different scenarios. To run tests:
```
python search.py tests/<filename> <method>
```

## Insights & Research

Analyzed efficiency and performance of different search methods.

Explored alternative heuristics and optimizations.

Considered an extended version where all destination nodes must be visited in the shortest path.

## Authors

Team Members: 
- Yasiru Lokesha 
- Prawud Rathnayake 
- Justin Tran
- Alex Vrsecky

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.edges = {}

    def add_edge(self, node, cost):
        self.edges[node] = cost

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, x, y):
        self.nodes[(x, y)] = Node(x, y)

    def add_edge(self, x1, y1, x2, y2, cost):
        if (x1, y1) in self.nodes and (x2, y2) in self.nodes:
            self.nodes[(x1, y1)].add_edge(self.nodes[(x2, y2)], cost)

def read_graph(filename):
    graph = Graph()
    with open(filename, 'r') as f:
        lines = f.readlines()
        node_section = False
        edge_section = False
        origin = None
        destinations = []
        for line in lines:
            if line.strip() == 'Nodes:':
                node_section = True
            elif line.strip() == 'Edges:':
                node_section = False
                edge_section = True
            elif line.strip() == 'Origin:':
                edge_section = False
            elif line.strip() == 'Destinations:':
                pass
            elif node_section:
                x, y = map(int, line.strip().split(': ')[1].strip('()').split(','))
                graph.add_node(x, y)
            elif edge_section:
                x1, y1, x2, y2, cost = line.strip().split(': ')[1].strip('()').split(',')
                x1, y1, x2, y2, cost = int(x1), int(y1), int(x2), int(y2), int(cost)
                graph.add_edge(x1, y1, x2, y2, cost)
            elif line.strip().startswith('Origin:'):
                origin = tuple(map(int, line.strip().split(': ')[1].strip('()').split(',')))
            elif line.strip().startswith('Destinations:'):
                destinations = [tuple(map(int, dest.strip('()').split(','))) for dest in line.strip().split(': ')[1].split(';')]
    return graph, origin, destinations

def dfs(graph, origin, destinations):
    visited = set()
    stack = [origin]
    while stack:
        node = stack.pop()
        if node in destinations:
            return node
        if node not in visited:
            visited.add(node)
            for neighbor in graph.nodes[node].edges:
                stack.append((neighbor.x, neighbor.y))
    return None

def bfs(graph, origin, destinations):
    visited = set()
    queue = [origin]
    while queue:
        node = queue.pop(0)
        if node in destinations:
            return node
        if node not in visited:
            visited.add(node)
            for neighbor in graph.nodes[node].edges:
                queue.append((neighbor.x, neighbor.y))
    return None

def gbfs(graph, origin, destinations):
    visited = set()
    queue = [origin]
    while queue:
        node = queue.pop(0)
        if node in destinations:
            return node
        if node not in visited:
            visited.add(node)
            for neighbor in graph.nodes[node].edges:
                queue.append((neighbor.x, neighbor.y))
    return None

def astar(graph, origin, destinations):
    visited = set()
    queue = [origin]
    while queue:
        node = queue.pop(0)
        if node in destinations:
            return node
        if node not in visited:
            visited.add(node)
            for neighbor in graph.nodes[node].edges:
                queue.append((neighbor.x, neighbor.y))
    return None

def cus1(graph, origin, destinations):
    visited = set()
    queue = [origin]
    while queue:
        node = queue.pop(0)
        if node in destinations:
            return node
        if node not in visited:
            visited.add(node)
            for neighbor in graph.nodes[node].edges:
                queue.append((neighbor.x, neighbor.y))
    return None

def cus2(graph, origin, destinations):
    visited = set()
    queue = [origin]
    while queue:
        node = queue.pop(0)
        if node in destinations:
            return node
        if node not in visited:
            visited.add(node)
            for neighbor in graph.nodes[node].edges:
                queue.append((neighbor.x, neighbor.y))
    return None

def main():
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> <method>")
        return
    filename = sys.argv[1]
    method = sys.argv[2]
    graph, origin, destinations = read_graph(filename)
    if method == 'DFS':
        result = dfs(graph, origin, destinations)
    elif method == 'BFS':
        result = bfs(graph, origin, destinations)
    elif method == 'GBFS':
        result = gbfs(graph, origin, destinations)
    elif method == 'A*':
        result = astar(graph, origin, destinations)
    elif method == 'CUS1':
        result = cus1(graph, origin, destinations)
    elif method == 'CUS2':
        result = cus2(graph, origin, destinations)
    else:
        print("Invalid method")
        return
    if result:
        print(f"Found Goal: {result}")
    else:
        print("Found Goal: None")

if __name__ == "__main__":
    main()

## File Format

The input files should follow this format:

```
Nodes:
1: (4,1)
2: (2,2)
...

Edges:
(2,1): 4
(3,1): 5
...

Origin:
2

Destinations:
5; 4
  
```
  
## Installation

### Clone this repository:
```
git clone https://github.com/](https://github.com/yasirulokesha/IntroToAI-Assignment-2.git
```

## Usage

Run the program using the following command:

```
python search.py <filename> <method>
```

Where:

`<filename>` is the path to the input file

`<method>` is one of DFS, BFS, GBFS, A*, CUS1, or CUS2

## Example
Executable file is provided in the repository. You can run it from the terminal using the following command:
```
python search.py <filename> <method>
```

Output Format
```
<filename> <method>
<goal> 
<number_of_nodes>
<path>
```
Example:
```
Searching the path using Custom 2 (Recursive Best First Search) Search...
PathFinder-test.txt CUS2

********* Search Results *********
Found Goal:      4
Node Visited:    3
Path:            2 -> 3 -> 4

```

## Testing

There has 10 test cases have been created to cover different scenarios. To run tests:
```
python search.py tests/<filename> <method>
```

## Insights & Research

Analyzed efficiency and performance of different search methods.

Explored alternative heuristics and optimizations.

Considered an extended version where all destination nodes must be visited in the shortest path.

## Authors

Team Members: 
- Yasiru Lokesha 
- Prawud Rathnayake 
- Justin Tran
- Alex Vrsecky

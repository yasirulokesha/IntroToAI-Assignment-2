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
```

## Outputs Results 

- Expected output
```
Searching the path using Custom 2 (Recursive Best First Search) Search...
PathFinder-test.txt CUS2

********* Search Results *********
Found Goal:      None
Node Visited:    1
Path:            4
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
input.txt A*
5 10
2 -> 3 -> 5
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

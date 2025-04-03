# IntroToAI-Assignment-2

##Tree-Based Search Algorithms for Route Finding

##Introduction

This project is an implementation of various tree-based search algorithms to solve the Route Finding Problem. The goal is to find optimal paths from an origin node to destination nodes in a 2D graph using both informed and uninformed search methods.

##Features

Implemented search algorithms:

*Depth-First Search (DFS)

*Breadth-First Search (BFS)

*Greedy Best-First Search (GBFS)

*A* Search (A*)

*Custom Uninformed Search (CUS1)

*Custom Informed Search (CUS2)

Reads graph data from structured text files

Supports batch testing via the command line

##Outputs results in a standard format

File Format

The input files should follow this format:

<pre>
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
  
</pre>
  
##Installation

##Clone this repository:

###git clone https://github.com/your-repo-name.git
###cd your-repo-name

Ensure Python is installed (if using Python).

Install required dependencies if any:

pip install -r requirements.txt

Usage

Run the program using the following command:

python search.py <filename> <method>

Where:

<filename> is the path to the input file

<method> is one of DFS, BFS, GBFS, A*, CUS1, or CUS2

Example

python search.py input.txt A*

Output Format

<filename> <method>
<goal> <number_of_nodes>
<path>

Example:

input.txt A*
5 10
2 -> 3 -> 5

Testing

At least 10 test cases have been created to cover different scenarios. To run tests:

python test_search.py

Insights & Research

Analyzed efficiency and performance of different search methods.

Explored alternative heuristics and optimizations.

Considered an extended version where all destination nodes must be visited in the shortest path.

##Authors

Team Members: 
Yasiru Lokesha 
Prawud Tharinda 
Justin Tran
Alex Vrsecky

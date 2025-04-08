import sys
import time
from problem import read_file
# from algorithms.algorithms import dfs

# Check the problem file and the algorithm 
if len(sys.argv) != 3:
    print("Usage: python search.py <filename> <method>")
    sys.exit(1)

# Get the filename and method from command line argument
filename = sys.argv[1]
method = sys.argv[2].upper()

# Parse the problem file
try:
    problem = read_file(filename)
    goal_node = problem.destinations
       
    # Print the graph 
    problem.graph.print_graph()
    
except Exception as e:
    print(f"Error parsing problem file: {e}")
    sys.exit(1)

# Choose the appropriate search algorithm
if method == "DFS":
    print("Searching the path using Depth-First Search...")
    # goal_node, path = dfs(problem)
elif method == "BFS":
    print("Searching the path using Bread-First Search...")
    # goal_node, path = bfs(problem)
elif method == "GBFS":
    print("Searching the path using Greedy Best-First  Search...")
    # goal_node, path = gbfs(problem)
elif method == "AS":
    print("Searching the path using Greedy A*('"'A-Star'"') Search...")
    # goal_node, path = a_star(problem)        
elif method == "CUS1":
    print("Searching the path using Greedy Custom 1 Search...")
    # goal_node, path = custom1(problem)
elif method == "CUS2":
    print("Searching the path using Greedy Custom 2 Search...")
    # goal_node, path = custom2(problem)
else:
    print(f"Unknown method: {method}")
    print("Available methods: DFS, BFS, GBFS, AS, CUS1, CUS2")
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> <method>")
        sys.exit(1)

# Print the result in the required format
if goal_node:
    print(f"{filename} {method}")
    print(f"{goal_node} ")
    # print(" ".join(str(node_id) for node_id in path))
else:
    print(f"No solution found for {filename} using {method}")
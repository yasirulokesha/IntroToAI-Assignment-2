import sys
from problem import read_file
from algorithms.depth_first_search import dfs
from algorithms.breadth_first_search import bfs
from algorithms.a_star_search import a_star
from algorithms.greedy_best_first_search import gbfs
from algorithms.custom1 import cus1
from algorithms.custom2 import cus2

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
    # problem.graph.print_graph()
except Exception as e:
    print(f"Error parsing problem file: {e}")
    sys.exit(1)
    
# Choose the appropriate search algorithm
if method == "DFS":
    print("Searching the path using Depth-First Search...")
    path, goal_node = dfs(problem)
    
elif method == "BFS":
    print("Searching the path using Bread-First Search...")
    path, goal_node = bfs(problem)
    
elif method == "GBFS":
    print("Searching the path using Greedy Best-First  Search...")
    path, goal_node = gbfs(problem)
    
elif method == "AS":
    print("Searching the path using Greedy A*('"'A-Star'"') Search...")
    path, goal_node = a_star(problem)    
        
elif method == "CUS1":
    print("Searching the path using Custom 1(Dijkstra's Algorithm) Search...")
    path, goal_node = cus1(problem)
    
elif method == "CUS2":
    print("Searching the path using Custom 2 (Recursive Best First Search) Search...")
    path, goal_node = cus2(problem)
    goal_node = str(goal_node).strip("[]").strip("''") 
    
else:
    print(f"Unknown method: {method}")
    print("Available methods: DFS, BFS, GBFS, AS, CUS1, CUS2")
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> <method>")
    sys.exit(1)

# Print the result in the required format
if goal_node:
    print(f"{filename} {method}")
    print(
        f"\n********* Search Results *********\nFound Goal:\t {goal_node}\nNode Visited:\t {len(path)}\nPath: \t\t {' -> '.join(path)}"
    )
        
else:
    print(f"No solution found for {filename} using {method}")
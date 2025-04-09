import sys
from problem import read_file
from algorithms.depth_first_search import dfs
from algorithms.breadth_first_search import bfs
from algorithms.a_star_search import a_star
from algorithms.custom1 import custom_search_1

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
    # path, goal_node = gbfs(problem)
    
elif method == "AS":
    print("Searching the path using Greedy A*('"'A-Star'"') Search...")
    path, goal_node = a_star(problem)    
        
elif method == "CUS1":
    print("Searching the path using Custom 1(Uniform Cost) Search...")
    # path, goal_node = custom1(problem)
    path, goal_node = custom_search_1(problem)
    
elif method == "CUS2":
    print("Searching the path using Greedy Custom 2 Search...")
    # path, goal_node = custom2(problem)
    
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
        f"\n********* Search Results *********\nFound Goal: {goal_node}\nNode Visited: ", len(path) ,"\nPath:" 
    )
    
    for i in range(len(path) - 1):
            print(path[i],end=" -> ")
            
    print(path[len(path)-1], "\n")
        
else:
    print(f"No solution found for {filename} using {method}")
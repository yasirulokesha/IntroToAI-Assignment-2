import sys
import time
from problem_parser import parse_problem_file
from search_algorithms import dfs, bfs, gbfs, astar, custom1, custom2

def main():
    # Check if the problem file and the algorithm are provided
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> <method>")
        sys.exit(1)
    
    # Get the filename and method from command line argument
    filename = sys.argv[1]
    method = sys.argv[2].upper()
    
    # Parse the problem file
    try:
        problem = parse_problem_file(filename)
    except Exception as e:
        print(f"Error parsing problem file: {e}")
        sys.exit(1)
    
    # Choose the appropriate search algorithm
    if method == "DFS":
        goal_node, path = dfs(problem)
    elif method == "BFS":
        goal_node, path = bfs(problem)
    elif method == "GBFS":
        goal_node, path = gbfs(problem)
    elif method == "AS":
        goal_node, path = astar(problem)
    elif method == "CUS1":
        goal_node, path = custom1(problem)
    elif method == "CUS2":
        goal_node, path = custom2(problem)
    else:
        print(f"Unknown method: {method}")
        print("Available methods: DFS, BFS, GBFS, AS, CUS1, CUS2")
        sys.exit(1)
    
    # Print the result in the required format
    if goal_node:
        print(f"{filename} {method}")
        print(f"{goal_node.id} {goal_node.nodes_created}")
        print(" ".join(str(node_id) for node_id in path))
    else:
        print(f"No solution found for {filename} using {method}")

if __name__ == "__main__":
    main()
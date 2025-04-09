import heapq

#performs Uniform Cost Search (UCS)
def custom_search_1(problem):
    graph = problem.graph
    start = problem.origin
    goals = problem.destinations

    priority_queue = [(0, start, [start])]
    visited = {}

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue) 

       #check if node i a goal, if node is goal return path and cost
        if node in goals:
            return path, cost  

        # checks if there is a lower cost path to the node
        if node not in visited or cost < visited[node]:
            visited[node] = cost

            # finds neighbors to the queue
            neighbors = sorted(graph.edges[node], key=lambda x: x[0])  # Sort by node ID
            for neighbor, edge_cost in neighbors:
                new_cost = cost + edge_cost
                heapq.heappush(priority_queue, (new_cost, neighbor, path + [neighbor]))

    return None, float("inf")  # No path found
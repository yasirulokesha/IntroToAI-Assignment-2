import heapq

# Performs A* Search with tie-breaking rules.
def a_star(problem):
    graph = problem.graph
    start = problem.origin
    goals = problem.destinations

    # Priority queue: (f, g, node, path)
    priority_queue = [(0, 0, start, [start])]  # (f, g, node, path)
    visited = {}

    while priority_queue:
        f, g, node, path = heapq.heappop(priority_queue)  # Expand lowest-cost node

        if node in goals:
            return path, g  # Goal reached, return path and cost

        if node not in visited or g < visited[node]:
            visited[node] = g  # Store the best known cost

            # Get neighbors, sort them in ascending order
            neighbors = sorted(graph.edges[node], key=lambda x: x[0])  # Sort by node ID
            for neighbor, edge_cost in neighbors:
                new_g = g + edge_cost  # Actual cost
                # h = min(euclidean_distance(neighbor, goal, graph) for goal in goals)  # Heuristic
                h = min(
                    graph.nodes[neighbor].distance_to(graph.nodes[goal]) for goal in goals
                )
                # print(graph.nodes[neighbor].distance_to(graph.nodes[goal])  for goal in goals)
                # f = new_g + h  # Total cost

                heapq.heappush(priority_queue, (f, new_g, neighbor, path + [neighbor]))

    return None, float("inf")  # No path found
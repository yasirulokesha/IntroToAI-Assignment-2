import math

#performs Recursive Best-First Search (RBFS)
def custom_search_2(problem):
    
    graph = problem.graph
    start = problem.origin
    goals = problem.destinations
    

    def rbfs(node, path, g, f_limit):
        if node in goals: 
            return path, g  #return path and cost if goal is reached

        # get neighbors and calculate f = g + h for every neighbor
        neighbors = []
        for neighbor, edge_cost in graph.edges[node]:
            if neighbor not in path:  
                new_g = g + edge_cost
                h = min(
                    graph.nodes[neighbor].distance_to(graph.nodes[goal]) for goal in goals
                )
                f = new_g + h
                neighbors.append((neighbor, new_g, f))

        if not neighbors:
            return None, math.inf  # No solution 

        # sort neighbors by f value
        neighbors.sort(key=lambda x: (x[2], x[0]))

        # explore neighbor with most potential
        while neighbors:
            best_neighbor, best_g, best_f = neighbors[0]
            if best_f > f_limit:
                return None, best_f  # returns if f exceeds limit

            #update 2nd best neighbor
            alternative_f = neighbors[1][2] if len(neighbors) > 1 else math.inf
            result, new_f = rbfs(best_neighbor, path + [best_neighbor], best_g, min(f_limit, alternative_f))

            if result is not None:
                return result, new_f  # found solution

            # update on the next best neighbor
            neighbors[0] = (best_neighbor, best_g, new_f)
            neighbors.sort(key=lambda x: (x[2], x[0]))

        return None, float('inf')  # No solution found

    # return to starting node
    path, cost = rbfs(start, [start], 0, math.inf)
    return path, cost
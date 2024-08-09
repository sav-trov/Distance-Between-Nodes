import time 

#code sourced from https://www.geeksforgeeks.org/python-nested-dictionary/
# and https://stackoverflow.com/questions/66774358/transforming-a-list-of-nodes-in-to-a-nested-dict-in-python
def distance_vector_routing(num_nodes, edges):
    neighbors = {j: {} for j in range(num_nodes)} #initilize a dictinary to store the cost to each neighbor node  
    for n1, n2, cost in edges:
        neighbors[n1][n2] = cost
        neighbors[n2][n1] = cost

    #code sourced from https://stackoverflow.com/questions/36903641/dijkstras-algorithm-with-shortest-path
    #intilize distance vector and path
    D = {j: float('inf') for j in range(num_nodes)}
    D[0] = 0

    #intitailize a path dictinary to store the path to each node
    path = {j: [] for j in range(num_nodes)}
    path[0] = [0]

    #code sourced from instructtion page on canvas and the book Computer Networking a Top Down Approach 
    #and https://stackoverflow.com/questions/47995901/implementing-bellman-ford-in-python
    #flag to check if there are any changes in the distance vector
    changed = True
    while changed:
        changed = False
        for node in range(num_nodes):
            for neighbor in neighbors[node]:
                 # bellman-ford equation / update the distance if shorter path is found
                if D[node] + neighbors[node][neighbor] < D[neighbor]:
                    D[neighbor] = D[node] + neighbors[node][neighbor]
                    path[neighbor] = path[node] + [neighbor]
                    changed = True

    return D, path

#code sourced from https://medium.com/@Doug-Creates/measure-python-program-execution-time-6c2646b096ba
def print_results(distances, paths, start_time):
    print("Distance Vector Routing:")
    for node in distances:
        if node != 0:
            path = '->'.join(map(str, paths[node]))
            print(f"shortest path to node {node} is {path} with cost {distances[node]}")
    print(f"Time Elapsed: {time.time() - start_time} seconds\n")


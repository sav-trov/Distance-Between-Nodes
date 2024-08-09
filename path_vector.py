import time 

#code sourced from https://www.geeksforgeeks.org/python-nested-dictionary/
# and https://stackoverflow.com/questions/66774358/transforming-a-list-of-nodes-in-to-a-nested-dict-in-python
def path_vector_routing(num_nodes, edges):
    #intialize dictinary to store the cost of each neighbor for each node 
    neighbors = {j: {} for j in range(num_nodes)}
    for n1, n2, cost in edges:
        neighbors[n1][n2] = cost
        neighbors[n2][n1] = cost

    #intialize a path dictinary to store the path to each node 
    paths = {j: [] for j in range(num_nodes)}
    for node in range(num_nodes):
        paths[node] = {node: [node]} #the path to each node intially ony contains itself

    #code sourced from instructtion page on canvas and the book Computer Networking a Top Down Approach
    #and https://github.com/Uninett/PyMetric/blob/master/model.py
    #flag to see if there are any changes in the path vectors 
    changed = True
    while changed:
        changed = False
        for node in range(num_nodes):
            for neighbor in neighbors[node]:
                for destination in paths[neighbor]:
                    #update to see if there is a shorter path
                    if destination not in paths[node] or len(paths[neighbor][destination]) + 1 < len(paths[node][destination]):
                        paths[node][destination] = [node] + paths[neighbor][destination]
                        changed = True

    #code sourced from instructtion page on canvas and the book Computer Networking a Top Down Approach
    #and  https://stackoverflow.com/questions/36903641/dijkstras-algorithm-with-shortest-path
    #calculate distance from paths 
    D = {j: float('inf') for j in range(num_nodes)}
    for node in range(num_nodes):
        if 0 in paths[node]: #if theres a path from the source node
            D[node] = len(paths[node][0]) - 1 #the distance 
    return D, paths

#code sourced from https://medium.com/@Doug-Creates/measure-python-program-execution-time-6c2646b096ba
def print_results(distances, paths, start_time):
    print("Path Vector Routing:")
    for node in distances:
        if node != 0: #skip the source node 
            path = '->'.join(map(str, paths[node][0]))
            print(f"shortest path to node {node} is {path} with cost {distances[node]}")
    print(f"Time Elapsed: {time.time() - start_time} seconds\n")


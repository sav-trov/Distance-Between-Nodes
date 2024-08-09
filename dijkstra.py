import time 
import heapq

#code sourced from https://www.geeksforgeeks.org/python-nested-dictionary/
# and https://stackoverflow.com/questions/66774358/transforming-a-list-of-nodes-in-to-a-nested-dict-in-python
def dijkstra_algorithm(num_nodes, edges):
    #intialize dictinary to store the cost of each neighbor for each node 
    neighbors = {j: {} for j in range(num_nodes)} 
    for n1, n2, cost in edges:
        neighbors[n1][n2] = cost
        neighbors[n2][n1] = cost

    #code sourced from https://stackoverflow.com/questions/36903641/dijkstras-algorithm-with-shortest-path
    #intilize the distance to infinity except for source node 
    D = {j: float('inf') for j in range(num_nodes)}
    D[0] = 0

    #initialize path dictinary to store the path to each node
    path = {j: [] for j in range(num_nodes)}
    path[0] = [0]

    #code sourced from instructtion page on canvas and the book Computer Networking a Top Down Approach 
    #and https://stackoverflow.com/questions/69580769/redundant-checks-in-python-implementation-of-dijkstras-algorithm
    #select the node with the least distance 
    pq = [(0, 0)]
    while pq:
        current_distance, node = heapq.heappop(pq)
        if current_distance > D[node]:
            continue
        for neighbor in neighbors[node]:
            distance = current_distance + neighbors[node][neighbor]
            if distance < D[neighbor]:
                D[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                path[neighbor] = path[node] + [neighbor]

    return D, path

#code sourced from https://medium.com/@Doug-Creates/measure-python-program-execution-time-6c2646b096ba
def print_results(distances, paths, start_time):
    print("Dijkstra's Algorithm:")
    for node in distances:
        if node != 0: #skip source node
            path = '->'.join(map(str, paths[node]))
            print(f"shortest path to node {node} is {path} with cost {distances[node]}")
    print(f"Time Elapsed: {time.time() - start_time} seconds\n")


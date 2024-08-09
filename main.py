import time
import sys
from distance_vector import distance_vector_routing, print_results as print_dv_results
from dijkstra import dijkstra_algorithm, print_results as print_dijkstra_results
from path_vector import path_vector_routing, print_results as print_pv_results

def read_topology(filename):
    #read topology from file 
    #code sourced from https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1204/handouts/py-file.html
    # and https://stackoverflow.com/questions/26853707/reading-from-file-in-python-with-splitting
    with open(filename, 'r') as file:
        num_nodes = int(file.readline().strip()) #first line is the number of nodes 
        edges = []
        for line in file:
            n1, n2, cost = line.strip().split()
            edges.append((int(n1), int(n2), float(cost))) #read each edge 
        return num_nodes, edges

def main(filename):
    num_nodes, edges = read_topology(filename)

    #run and meausure  distance vector routing 
    # code sourced from https://stackoverflow.com/questions/23437700/graph-shortest-paths-w-dynamic-weights-repeated-dijkstra-distance-vector-routi
    start_time = time.time()
    distances, paths = distance_vector_routing(num_nodes, edges)
    print_dv_results(distances, paths, start_time)

    #run and measure dijkstra's algorithm
    start_time = time.time()
    distances, paths = dijkstra_algorithm(num_nodes, edges)
    print_dijkstra_results(distances, paths, start_time)

    #run and measure path vector routing
    start_time = time.time()
    distances, paths = path_vector_routing(num_nodes, edges)
    print_pv_results(distances, paths, start_time)

#code sourced from https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    #print arguments  for debugging 
    if len(sys.argv) != 2: #ensure argument is provided 
        print("Usage: python main.py <topology_file>")
        sys.exit(1)
    filename = sys.argv[1]
    main(filename)


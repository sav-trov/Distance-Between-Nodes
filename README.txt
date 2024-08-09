	This programming assignment implements the routing algorithms, Distance Vector Routing, Dijkstra’s Algorithm, and Path Vector Routing.
These algorithms are used to calculate the shortest path from a source node to the other nodes in the network depending on the text file 
containing the network topology. The text file list the number of nodes and the edges with the cost. 

	The Distance Vector Routing starts by each node initializing its distance vector with infinity values except for the source node which 
is set to 0. Then the algorithm uses the nodes to iteratively exchange the distance vectors with there neighbors. To update the distance
we use the Bellman-Ford equation which is D[y]=min(D[y],D[x]+c[x][y]). The ‘D[y] is the distance of the shortest distance to node y, 
‘D[x] is the distance to node x, and c[x][y] is the cost of the edge from x to y. The last step is to end the code when there are no 
more updates to the total distance. The complexity of this is O(N^2).

	The Dijkstra’s Algorithm start by setting each node’s distance to infinity, except for the source node which is set to 0. A priority 
que is used to select the node with the minimum distance. Then the algorithm starts by adding up the nodes on a tree based on the shortest 
distance. To find the distance of the neighboring nodes we use the equation: D[x]=min(D[x],D[w]+c[w][x]). “D[x]” is the distance to node x.
D[w] is the distance to node w, and c[w][x] Is the cost of the edge from w to x. The last step is to end the code when all the nodes are
included in the tree. The complexity for this code is O((V+E)logV).

	The Path Vector Routing starts by initializing each node to its path vector with paths to itself or neighbors. Then the algorithm 
starts with nodes exchanging path vectors with their neighbors. The paths are updated throughout, the equation used is:
Path[y] = Best(Path[y],myself+Pathw[y]). Path[y] is the path to node y and Pathw[y] is the path from neighbor w to node y. 
The last step is to end the code when no updates occur. The complexity for this code is O(N^3).

	The command I used to run this code was “python3 ‘/home/savanna/Desktop/main.py’ ‘/home/savanna/Desktop/network_topology.txt’”
I ran this code in a Virtual Machine.

# ITCS6114_Project2
##ITCS-6114 Project 2 - M.B.Curlee
This project demonstrates some algorithm fundamentals including:
  1. Singles-source shortest path algorithm
  2. Minimum Spanning Tree (MST)
  3. Strongly Connected Components (SSCs)
I chose to demonstrate this process in jupyter notebook as this provides a viable and clean way to both display code and describe the implementation. Examples were implemented from demonstrated algorithms in class.

#Problem 1: Single-source Shortest Path Algorithm

Find shortest path tree in both directed and undirected weighted graphs for a given source vertex. Assume there is no negative edge in your graph. You will print each path and path cost for a given source.

I chose several graphs from the internet that looked visually interesting. I then transposed them into text files attached to this implementation and resembling the following, with line 1 indicating the number of vertices, edges and U or D to describe directed or undirected. The middle lines contain the starting node, the ending node and the weight/distance between. The final line is the starting node.

Dikstra
Dikstra's algorithm provides a clean method for determining the shortest path from a starting node and any other node, by traversing the lowest cost path. The idea is to continiously calculate the shortest distance from start to end, while excluding longer distances/weights when making updates. The algorithm works as follows:

Initialization of all nodes with distance "infinite"; initialization of the starting node with 0
Marking of the distance of the starting node as permanent, all other distances as temporarily.
Setting of starting node as active.
Calculation of the temporary distances of all neighbour nodes of the active node by summing up its distance with the weights of the edges.
If such a calculated distance of a node is smaller as the current one, update the distance and set the current node as antecessor. This step is also called update and is Dijkstra's central idea.
Setting of the node with the minimal temporary distance as active. Mark its distance as permanent.
Repeating of steps 4 to 7 until there aren't any nodes left with a permanent distance, which neighbours still have temporary distances.
Dikstra's algorithm runs with an expected runtime of (m+n)(log(n).

My Implementation
I chose to use python for my implementation as defaultdict(list) addapts nicely to the unequal size of internal lists. In this implementation, I could find no real measurable increase in time complexity with operations dedicated to creating or maintaining the lists. I found that many of the graphs I decided to use worked perfectly for this implementation.

Problem 2: Minimum Spanning Tree Algorithm

Given a connected, undirected, weighted graph, find a spanning tree using edges that minimizes the total weight. Use either Kruskal's or Prim's algorithm to find Minimum Spanning Tree (MST). You will printout edges of the tree and total cost of minimum spanning tree

Kruskal
Kruskal's algorithm is stated as a greedy algorithm that finds local minimums in an attempt to find an overal global minimum for a spanning tree graph.

We start from the edges with the lowest weight and keep adding edges until we reach our goal.

The steps for implementing Kruskal's algorithm are as follows:

Sort all the edges from low weight to high
Take the edge with the lowest weight and add it to the spanning tree. If adding the edge created a cycle, then reject this edge.
Keep adding edges until we reach all vertices.
My Implementation
I used the same setup for defaultdict(list) in this implementation as noted above. Here again I could find no real time complexity increase by using these lists, in terms of measured microseconds. Kruskal's runs with an expected time complexity of nlogn. I found that the graphs I chose for this project may have been too highly connected and may not have been a good representative of the overall capability of this algorithm.

Problem 3: Finding Strongly Connected Components

Given a directed graph with vertices and edges. This graph may not be simple. Decompose this graph into Strongly Connected Components (SCCs) and print the components. You can use the same input format defined below.

Strongly Connected Components
A directed graph is strongly connected if there is a path between all pairs of vertices. A strongly connected component (SCC) of a directed graph is a maximal strongly connected subgraph. To find these components, one must first transverse a graph using either DFS or BFS with connected nodes being added to a list. The graph is then transposed and again transversed to find those nodes that are connected in both directions.

My Implementation
I again found that the graphs used in my implementation may have been too robust. I found also that most (and all in some cases) of my nodes were connected. I attribute this to the complex graphs that I chose for this implementation. Time complexity in this implementation was increased by the use of my lists in this case, as there were more lists per run than in the previous sections.

For running this implentation, all files needed are present in the 'Code' folder. The Project2 file is the helper file, with individual files for each requirement. There is, as well, a util file that contains much of the visualization coding and brings everything together. 

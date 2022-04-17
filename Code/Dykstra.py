from collections import defaultdict
import time
import pandas as pd

class dGraph:
    def __init__(self, directed):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdge(self, beg, end, wt):
        self.graph[beg].append([end, wt])

        if self.directed is False:
            self.graph[end].append([beg, wt])
        elif self.directed is True:
            self.graph[end] = self.graph[end]

    def find_min(self, dist, visited):
        min = float('inf')
        index = -1
        for vert in self.graph.keys():
            if visited[vert] is False and dist[vert] < min:
                min = dist[vert]
                index = vert

        return index

    def Dikstra(self, start):
        visited = {i: False for i in self.graph}
        dist = {i: float('inf') for i in self.graph}
        parent = {i: None for i in self.graph}

        dist[start] = 0

        # find shortest path for all vertices
        for i in range(len(self.graph) - 1):
            u = self.find_min(dist, visited)
            visited[u] = True
            for v, w in self.graph[u]:

                if visited[v] is False and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u
        return parent, dist

    def printPath(self, parent, v):
        if parent[v] is None:
            return
        self.printPath(parent, parent[v])
        print(v,end=" ")

    def printSolution(self, dist, parent, start):
        print('{}\t\t{}\t{}'.format('Vertex', 'Distance', 'Path'))

        for i in self.graph.keys():
            if i == start:
                continue
            if  dist[i]==float("inf"):
                continue
            src = ord(start)-65
            print('{} -> {}\t\t{}\t\t{}'.format(start, i, dist[i], start), end=' ')
            self.printPath(parent, i)
            print()

    
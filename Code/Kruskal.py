import time
from collections import defaultdict

class kGraph:

    def __init__(self, vertices):
        self.V = int(vertices)
        self.graph = []


    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root

        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def KruskalMST(self):

        result = []
        e = 0
        i = 0
        self.graph = sorted(self.graph, key=lambda x: x[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        nodes = []
        while e < self.V - 1:
            nodes.append(chr(i+65))
            u, v, w = self.graph[i]

            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        print('This graph contained the following nodes:')
        print(nodes)
        print('\033[1m' + "Edge-Child \t\t Weight" + '\033[0m')
        print()
        res=0
        for u, v, weight in result:
            print(chr(u + 65), "-", chr(v + 65), "\t\t\t", weight)
            res+=weight
        print('\033[1m'+"The total Cost for Minimum Spanning Tree is", res,'\033[0m')




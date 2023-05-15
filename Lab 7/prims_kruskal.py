from collections import defaultdict
import random
import sys
import time
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.adj = defaultdict(list)

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
        self.adj[u].insert(0, [v, w])
        self.adj[v].insert(0, [u, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def KruskalMST(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)

    def PrimMST(self):
        V = self.V
        key = []
        parent = []

        for v in range(V):
            parent.append(-1)
            key.append(sys.maxsize)

        key[0] = 0

        mstSet = [False] * self.V

        parent[0] = -1

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v, weight in self.adj[u]:
                if weight > 0 and mstSet[v] == False and key[v] > weight:
                    key[v] = weight
                    parent[v] = u

        self.printMST(parent)

    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][2])


graph_dense = Graph(100)
for i in range(100):
    for j in range(100):
        if j > i:
            graph_dense.addEdge(i, j, random.randint(1, 100))

graph_sparse = Graph(100)
for i in range(100):
    for j in range(100):
        if j > i and random.randint(1, 100) < 30:
            graph_sparse.addEdge(i, j, random.randint(1, 100))

graph_dense2 = Graph(1000)
for i in range(1000):
    for j in range(1000):
        if j > i:
            graph_dense2.addEdge(i, j, random.randint(
                1, 100))

graph_sparse2 = Graph(1000)
for i in range(1000):
    for j in range(1000):
        if j > i and random.randint(1, 100) < 30:
            graph_sparse2.addEdge(i, j, random.randint(
                1, 100))

kruskal = []
prims = []

start = time.time()
graph_dense.KruskalMST()
end = time.time()
kruskal.append(end - start)

start = time.time()
graph_sparse.KruskalMST()
end = time.time()
kruskal.append(end - start)

start = time.time()
graph_dense2.KruskalMST()
end = time.time()
kruskal.append(end - start)

start = time.time()
graph_sparse2.KruskalMST()
end = time.time()
kruskal.append(end - start)

start = time.time()
graph_dense.PrimMST()
end = time.time()
prims.append(end - start)

start = time.time()
graph_sparse.PrimMST()
end = time.time()
prims.append(end - start)

start = time.time()
graph_dense2.PrimMST()
end = time.time()
prims.append(end - start)

start = time.time()
graph_sparse2.PrimMST()
end = time.time()
prims.append(end - start)

plt.figure(1)
plt.bar(['Sparse Graph with 100 Vertices', 'Dense Graph with 100 Vertices', 'Sparse Graph with 1000 Vertices', 'Dense Graph with 1000 Vertices'],
        [prims[1], prims[0], prims[3], prims[2]], color='green')
plt.title('Prim Algorithm Runtime')
plt.ylabel('Time in seconds')

plt.figure(2)
plt.bar(['Sparse Graph with 100 Vertices', 'Dense Graph with 100 Vertices', 'Sparse Graph with 1000 Vertices', 'Dense Graph with 1000 Vertices'],
        [kruskal[1], kruskal[0], kruskal[3], kruskal[2]], color='red')
plt.title('Kruskal Algorithm Runtime')
plt.ylabel('Time in seconds')

plt.show()

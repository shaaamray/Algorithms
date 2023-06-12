import sys

class Graph:
    def __init__(self, vertices):
        self.nodes = vertices
        self.graph = [[0 for i in range(vertices)] for j in range(vertices)]

    def add(self, src, dst, wght):
        self.graph[src][dst] = wght
        self.graph[dst][src] = wght

    def min_node_finder(self, values, mst_set):
        min_node = None
        min_val = sys.maxsize
        for i in range(self.nodes):
            if not mst_set[i] and min_val > values[i]:
                min_val = values[i]
                min_node = i
        return min_node

    def prims(self):
        values = [sys.maxsize] * self.nodes
        parent = [None] * self.nodes
        mst_set = [False] * self.nodes
        values[0] = 0
        parent[0] = -1
        
        # find node with the minimum edge distance
        for i in range(self.nodes):
            u = self.min_node_finder(values, mst_set)

            mst_set[u] = True
            
            #update other nodes values and roots/parent
            for v in range(self.nodes):
                if self.graph[u][v] > 0 and not mst_set[v] and self.graph[u][v] < values[v]:
                    values[v] = self.graph[u][v]
                    parent[v] = u
                    
        mst_cost = 0
        for i in range(1, self.nodes):
            print(parent[i], "-", i, "\t", values[i])
            mst_cost += values[i]
        
        print("MST cost is", mst_cost, "\n")


g = Graph(4)
g.add(0, 1, 10)
g.add(0, 2, 6)
g.add(0, 3, 5)
g.add(2, 3, 4)
g.add(1, 3, 15)
g.prims()

h = Graph(5)
h.add(0, 1, 2)
h.add(0, 3, 6)
h.add(1, 2, 3)
h.add(1, 3, 8)
h.add(1, 4, 5)
h.add(2, 4, 7)
h.add(3, 4, 9)
h.prims()

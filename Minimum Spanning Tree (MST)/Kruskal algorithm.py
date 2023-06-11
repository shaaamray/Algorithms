class Graph:
    def __init__(self, vertices):
        self.nodes = vertices
        self.graph = []

    def add(self, src, dst, wght):
        self.graph.append([src, dst, wght])

    # will use union-find algorithm or disjoint set data structure

    def find(self, parent, node):
        # basically finding the root node of corresponding node
        if parent[node] != node:
            parent[node] = self.find(parent, parent[node])
        return parent[node]

    # assinging root node among two nodes
    def union(self, parent, rank, p1, p2):
        if rank[p1] > rank[p2]:
            parent[p2] = p1
        elif rank[p1] < rank[p2]:
            parent[p1] = p2
        else:
            parent[p2] = p1
            rank[p1] += 1

    def kruskal(self):
        mst = []
        parent = []
        rank = []
        n, e = 0, 0

        self.graph = sorted(self.graph, key=lambda i: i[2])

        for i in range(self.nodes):
            parent.append(i)
            rank.append(0)

        while e < self.nodes - 1:
            u, v, w = self.graph[n]
            n += 1
            # finding root nodes--> parent1, parent2
            p1 = self.find(parent, u)
            p2 = self.find(parent, v)

            # if roots are different then merging will not create a cycle
            if p1 != p2:
                mst.append([u, v, w])
                e += 1  # increasing edge
                self.union(parent, rank, p1, p2)

        mst_cost = 0
        print("Source", "Destination", "Weight")
        for u, v, w in mst:
            mst_cost += w
            print("%d --> %d == %d" % (u, v, w))
        print("MST is", mst_cost)


g = Graph(4)
g.add(0, 1, 10)
g.add(0, 2, 6)
g.add(0, 3, 5)
g.add(1, 3, 15)
g.add(2, 3, 4)
g.kruskal()

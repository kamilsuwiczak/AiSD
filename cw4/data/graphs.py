class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def print_graph(self):
        for vertex in self.graph:
            print(vertex, "->", " -> ".join(str(x) for x in self.graph[vertex]))

# Create a new graph
g = Graph()

# Add edges to the graph
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(5, 1)
g.add_edge(3, 4)

# Print the graph
g.print_graph()
xd = {}
xd[1] = 2
xd[3] = 5
xd[2] = 4
print(xd)
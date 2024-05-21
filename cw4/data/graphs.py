import random
import networkx as nx
import matplotlib.pyplot as plt

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
 
    def generate_hamiltonian_graph(self, num_vertices, saturation):
        if num_vertices < 3:
            return
        num_edges = int(num_vertices*(num_vertices-1)/2 * saturation)
        if num_edges < num_vertices:
            num_edges = num_vertices
        vertices = list(range(1, num_vertices + 1))
        random.shuffle(vertices)
        for i in range(num_vertices - 1):
            self.add_edge(vertices[i], vertices[i + 1])

        self.add_edge(vertices[num_vertices - 1], vertices[0])

    def draw_graph(self):
        G = nx.Graph()
        for vertex in self.graph:
            for edge in self.graph[vertex]:
                G.add_edge(vertex, edge)
        
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()

g = Graph()
    
g.generate_hamiltonian_graph(7)
g.draw_graph()
g.print_graph()

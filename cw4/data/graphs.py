import random
import networkx as nx
import matplotlib.pyplot as plt
import math

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
    
    def remove_edge(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def generate_hamiltonian_graph(self, num_vertices, saturation):
        if num_vertices < 3:
            return
        num_edges = int(num_vertices*(num_vertices-1)/2 * saturation)
        if num_edges < num_vertices:
            num_edges = num_vertices
        vertices = list(range(1, num_vertices + 1))
        
        random.shuffle(vertices)
        for i in range(num_vertices - 1):               #generowanie cyklu Hamiltona
            self.add_edge(vertices[i], vertices[i + 1])
            num_edges -= 1
        self.add_edge(vertices[num_vertices - 1], vertices[0])
        num_edges -= 1

        while num_edges > 0:
            u = random.choice(vertices)
            v = random.choice(vertices)
            if u != v and v not in self.graph[u]:
                self.add_edge(u, v)
                num_edges -= 1
    
    def generate_non_hamiltonian_graph(self, num_vertices):
        self.generate_hamiltonian_graph(num_vertices-1, 0.5)
        self.graph[num_vertices] = []
    
    def find_eulerian_cycle(self):
        for vertex in self.graph:
            if len(self.graph[vertex]) % 2 != 0:
                return None

        G = self.graph.copy()
        start_vertex = next(iter(G))
        stack = [start_vertex]
        path = []

        while stack:
            u = stack[-1]
            if G[u]:
                v = G[u][0]
                stack.append(v)
                self.remove_edge(u, v)
            else:
                path.append(stack.pop())
        return path


    def draw_graph(self):
        G = nx.Graph()
        for vertex in self.graph:
            for edge in self.graph[vertex]:
                G.add_edge(vertex, edge)
        nx.draw(G, with_labels=True, font_weight='bold', node_size=1000, font_size=10, node_color='skyblue', edge_color='black', width=1.5, edge_cmap=plt.cm.Blues)
        graph = plt.gcf()
        graph.canvas.manager.set_window_title('Graph')
        plt.show()

    def export_graph(self, file_name='graph.tex'):
        with open(file_name, 'w') as f:
            f.write('\\documentclass{standalone}\n')
            f.write('\\usepackage{tikz}\n')
            f.write('\\begin{document}\n')
            f.write('\\begin{tikzpicture}[scale=2]\n')
            
            vertices = list(self.graph.keys())
            n = len(vertices)
            positions = {}
            radius = 3

            for i, vertex in enumerate(vertices):
                angle = 2 * math.pi * i / n
                x = radius * math.cos(angle)
                y = radius * math.sin(angle)
                positions[vertex] = (x, y)
                f.write(f'\\node[draw, circle] ({vertex}) at ({x:.2f}, {y:.2f}) {{{vertex}}};\n')
            
            for vertex in self.graph:
                for neighbor in self.graph[vertex]:
                    if vertex < neighbor:
                        f.write(f'\\draw ({vertex}) -- ({neighbor});\n')
            
            f.write('\\end{tikzpicture}\n')
            f.write('\\end{document}\n')

def main():
    pass
    # g = Graph()
        
    # # g.generate_non_hamiltonian_graph(7)
    # g.generate_hamiltonian_graph(9, 0.5)
    # # g.draw_graph()
    # g.print_graph()
    
    # print("cykl Eulera: ",g.find_eulerian_cycle())

if __name__ == "__main__":
    main()
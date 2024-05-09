import random

class Graph:
    def __init__(self, vertices):
        self.num_vertices = vertices
        self.adjacency_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        self.successor_list = [[] for _ in range(self.num_vertices)]
        self.edge_list = []

    def add_edge(self, source, destination):
        if 1 <= source <= self.num_vertices and 1 <= destination <= self.num_vertices:
            self.adjacency_matrix[source - 1][destination - 1] = 1
            self.successor_list[source - 1].append(destination)
            self.edge_list.append((source, destination))
    

    def print_matrix(self):
        print("  | ", end="")
        for i in range(self.num_vertices):
            print(i + 1, end=" ")
        print()
        print(' '+"==" * (self.num_vertices + 1))
        for i in range(self.num_vertices):
            print(i + 1, "| ", end="")
            for j in range(self.num_vertices):
                print(self.adjacency_matrix[i][j], end=" ")
            print()

    def print_successor_list(self):
        for i in range(self.num_vertices):
            print(i + 1, ": ", end="")
            for successor in self.successor_list[i]:
                print(successor, end=" ")
            print()
    
    def print_edge_list(self):
        for edge in self.edge_list:
            print(f"{edge[0]} -> {edge[1]}")

    def find_edge(self, source, destination, representation):
        if representation == "matrix":
            if self.adjacency_matrix[source-1][destination-1] == 1:
                return True
            else:
                return False
        elif representation == "list":
            if len(self.successor_list[source-1]) < destination:
                return False
            else:
                if self.successor_list[source-1][destination-1] == destination:
                    return True
                else:
                    return False
    
    def search(self, start, representation, method):
        start -= 1
        visited = [False] * self.num_vertices
        array = []
        array.append(start)
        visited[start] = True
        if method == "BFS": #array -> queue
            x = 0
        elif method == "DFS": #array -> stack
            x = -1      

        while array:
            start = array.pop(x)    
            print(start + 1, end=" ")

            if representation == "matrix":
                for i in range(self.num_vertices):
                    if self.adjacency_matrix[start][i] == 1 and visited[i] == False:
                        array.append(i)
                        visited[i] = True

            elif representation == "list":
                for i in self.successor_list[start]:
                    if visited[i-1] == False:
                        array.append(i-1)
                        visited[i-1] = True

            elif representation == "table":
                for i in self.edge_list:
                    if i[0] == start+1 and visited[i[1]-1] == False:
                        array.append(i[1]-1)
                        visited[i[1]-1] = True
        print()
        
    def khan_topological_sort(self):
        # Step 1: Compute in-degrees of all vertices
        result = []
        in_degrees = [0] * self.num_vertices
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.adjacency_matrix[i][j] == 1:
                    in_degrees[j] += 1
        
        # Step 2: Initialize an empty queue and enqueue all vertices with in-degree 0
        queue = []
        for i in range(self.num_vertices):
            if in_degrees[i] == 0:
                queue.append(i)
        
        # Step 3: Process the queue until it becomes empty
        while queue:
            vertex = queue.pop(0)
            result.append(vertex+1)
            
            # Decrease the in-degree of adjacent vertices and enqueue them if their in-degree becomes 0
            for i in range(self.num_vertices):
                if self.adjacency_matrix[vertex][i] == 1:
                    in_degrees[i] -= 1
                    if in_degrees[i] == 0:
                        queue.append(i)
        if len(result) == self.num_vertices:
            print(*result)
        else:
            print("Graf zawiera cykl!")


    def generate_acyclic_graph(self, saturation):
        num_edges = int((saturation * self.num_vertices * (self.num_vertices - 1)) / 2)
        edges = set()
        
        while len(edges) < num_edges:
            source = random.randint(1, self.num_vertices)
            destination = random.randint(1, self.num_vertices)
            
            if source != destination:
                edges.add((source, destination))
        
        for edge in edges:
            graph.add_edge(edge[0], edge[1])
    
    def export_graph(self, layout='circle'):
        output = "\\begin{tikzpicture}[>=stealth, ->]\n"
        if layout == 'circle':
            angle_step = 360 / self.num_vertices
            for i in range(1, self.num_vertices + 1):
                angle = (i - 1) * angle_step
                output += f"\\node (v{i}) at ({angle}:3cm) {{{i}}};\n"
        elif layout == 'grid':
            rows = int(self.num_vertices ** 0.5) + 1
            for i in range(1, self.num_vertices + 1):
                x = (i - 1) % rows
                y = (i - 1) // rows
                output += f"\\node (v{i}) at ({x}, {y}) {{{i}}};\n"

        for edge in self.edge_list:
            source, destination = edge
            output += f"\\draw (v{source}) -> (v{destination});\n"

        output += "\\end{tikzpicture}\n"
        
        return output

    

    

if __name__ == "__main__":
    graph = Graph(5)

    graph.generate_acyclic_graph(0.5)
    
    


    graph.print_matrix()
    graph.print_successor_list()
    print(graph.successor_list)

    graph.search(1,"matrix","BFS")
 
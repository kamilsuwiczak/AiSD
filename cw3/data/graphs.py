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
    
            
        

if __name__ == "__main__":
    graph = Graph(5)

    graph.add_edge(1, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 1)
    graph.add_edge(4, 2)

    graph.print_matrix()
    graph.print_successor_list()
    print(graph.find_edge(4,1, "list"))

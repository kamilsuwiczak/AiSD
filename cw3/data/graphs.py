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
    
    def BFS(self, start,representation):
        start = start - 1
        visited = [False] * self.num_vertices
        queue = []
        queue.append(start)
        visited[start] = True
        while queue:
            start = queue.pop(0)
            print(start + 1, end=" ")
            if representation == "matrix":
                for i in range(self.num_vertices):
                    if self.adjacency_matrix[start][i] == 1 and visited[i] == False:
                        queue.append(i)
                        visited[i] = True
            elif representation == "list":
                for i in self.successor_list[start]:
                    if visited[i-1] == False:
                        queue.append(i-1)
                        visited[i-1] = True
            elif representation == "table":
                for i in self.edge_list:
                    if i[0] == start+1 and visited[i[1]-1] == False:
                        queue.append(i[1]-1)
                        visited[i[1]-1] = True
            


    def DFS(self, start,represenation):
        start = start - 1
        visited = [False] * self.num_vertices
        stack = []
        stack.append(start)
        visited[start] = True
        while stack:
            start = stack.pop()
            print(start+1, end=" ")
            if represenation == "matrix":
                for i in range(self.num_vertices):
                    if self.adjacency_matrix[start][i] == 1 and visited[i] == False:
                        stack.append(i)
                        visited[i] = True
            elif represenation == "list":
                for i in self.successor_list[start]:
                    if visited[i-1] == False:
                        stack.append(i-1)
                        visited[i-1] = True 
            elif represenation == "table":
                for i in self.edge_list:
                    if i[0] == start+1 and visited[i[1]-1] == False:
                        stack.append(i[1]-1)
                        visited[i[1]-1] = True 

    

    

if __name__ == "__main__":
    graph = Graph(7)

    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 6)
    graph.add_edge(3, 7)


    graph.print_matrix()
    graph.print_successor_list()

    graph.DFS(1,"table")
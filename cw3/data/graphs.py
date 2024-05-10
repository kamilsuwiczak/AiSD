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
        elif representation == "table":
            for i in self.edge_list:
                if i[0] == source and i[1]==destination:
                    return True
    
    def least_in_degree(self):
        in_degrees = [0] * self.num_vertices
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.adjacency_matrix[i][j] == 1:
                    in_degrees[j] += 1
        
        min_in_degree = min(in_degrees)
        vertices = [i+1 for i, degree in enumerate(in_degrees) if degree == min_in_degree]
        
        return vertices
       
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
        
    def khan_sort(self, representation):
        result = []
        in_degrees = [0] * self.num_vertices
        
        if representation == "matrix":
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    if self.adjacency_matrix[i][j] == 1:
                        in_degrees[j] += 1
            queue = []
            for i in range(self.num_vertices):
                if in_degrees[i] == 0:
                    queue.append(i)
            
            while queue:
                vertex = queue.pop(0)
                result.append(vertex+1)
                for i in range(self.num_vertices):
                    if self.adjacency_matrix[vertex][i] == 1:
                        in_degrees[i] -= 1
                        if in_degrees[i] == 0:
                            queue.append(i)
            if len(result) == self.num_vertices:
                print(*result)
            else:
                print("Graf zawiera cykl!")
    
        elif representation == "list":
            for i in range(self.num_vertices):
                for j in self.successor_list[i]:
                    in_degrees[j-1] += 1
            queue = []
            for i in range(self.num_vertices):
                if in_degrees[i] == 0:
                    queue.append(i)
            
            while queue:
                vertex = queue.pop(0)
                result.append(vertex+1)
                for i in self.successor_list[vertex]:
                    in_degrees[i-1] -= 1
                    if in_degrees[i-1] == 0:
                        queue.append(i-1)
            if len(result) == self.num_vertices:
                print(*result)
            else:
                print("Graf zawiera cykl!")

        elif representation == "table":
            for i in self.edge_list:
                in_degrees[i[1]-1] += 1
            queue = []
            for i in range(self.num_vertices):
                if in_degrees[i] == 0:
                    queue.append(i)
            
            while queue:
                vertex = queue.pop(0)
                result.append(vertex+1)
                for i in self.edge_list:
                    if i[0] == vertex+1:
                        in_degrees[i[1]-1] -= 1
                        if in_degrees[i[1]-1] == 0:
                            queue.append(i[1]-1)
            if len(result) == self.num_vertices:
                print(*result)
            else:
                print("Graf zawiera cykl!")
    
    def export_graph(self, layout='circle'):
        output = "\\begin{tikzpicture}[>=stealth, ->]\n"

        if layout == 'circle':
            angle_step = 360 / self.num_vertices
            for i in range(1, self.num_vertices + 1):
                angle = (i - 1) * angle_step
                output += f"\\node (v{i}) at ({angle}:6cm) {{{i}}};\n"
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


    def tarjan_sort(self):
        visited = [False] * self.num_vertices
        stack = []
        result = []

        def dfs_list(vertex):
            visited[vertex] = True
            for neighbor in self.successor_list[vertex]:
                if not visited[neighbor - 1]:
                    dfs_list(neighbor - 1)
            stack.append(vertex+1)
        
        def dfs_matrix(vertex):
            visited[vertex] = True
            for i in range(self.num_vertices):
                if self.adjacency_matrix[vertex][i] == 1 and not visited[i]:
                    dfs_matrix(i)
            stack.append(vertex+1)
        
        def dfs_table(vertex):
            visited[vertex] = True
            for edge in self.edge_list:
                if edge[0] == vertex+1 and not visited[edge[1]-1]:
                    dfs_table(edge[1]-1)
            stack.append(vertex+1)

        for i in range(self.num_vertices):
            if not visited[i]:
                dfs_list(i)
    
        while stack:
            result.append(stack.pop())
        
        print(*result)
       

        

if __name__ == "__main__":
    graph = Graph(4)

    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4,1)    
    
    
    graph.print_matrix()
    graph.print_successor_list()

    graph.tarjan_sort()
    graph.khan_sort("list")
 
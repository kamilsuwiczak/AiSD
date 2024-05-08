import graphs
import sys
import math

def printing_help():
    print("help\t\tshows this message")
    print("print\t\tasks user what graph representation should be printed and print it")
    print("find_edge\tfinds if edge between two vertices exits")
    print("BFS\t\tprints graph in breath-first-search way")
    print("DFS\t\tprints graph in depth-first-search way")
    print("exit\t\texits the program")

def menu(representation):
    action = input("action> ")
    match action:
        case "help":
            printing_help()
        
        case "print":
            match representation:
                case "matrix":
                    graph.print_matrix()
                case "list":
                    graph.print_successor_list()
                case "table":
                    graph.print_edge_list()

        case "find_edge":
            source = int(input("from> "))
            destination = int(input("to> "))
            if graph.find_edge(source, destination, representation) == True:
                print(f'edge ({source}, {destination}) exists')
            else:
                print(f'edge ({source}, {destination}) does not exist')


        case "BFS":
            num_incoming_edges=[]
            for _ in range(0,num_nodes):
                num_incoming_edges.append(0)
            if representation == "matrix":
                print(graph.adjacency_matrix)
                for row in graph.adjacency_matrix:
                    for col in range(0,len(row)):
                        if row[col] == 1:
                            num_incoming_edges[col] +=1
            print(num_incoming_edges)
            print(min(num_incoming_edges))
        
        case "DFS":
            pass

        case "exit":
            sys.exit(1)

# działa i heredoc (python3 main.py --user-provided << EOF) też działa
if sys.argv[1] == "--user-provided":
    try:
        num_nodes = int(input("nodes> "))
        if num_nodes <0:
            raise ValueError
    except:
        print("Niewłaściwe dane")
        sys.exit(1)

    graph = graphs.Graph(num_nodes)
    for i in range(1, num_nodes+1):
        vertices = input(f'{i}> ').split()
        for j in vertices:
            try:
                if int(j) <=0:
                    raise ValueError
            except:
                print("Niewłaściwe dane")
                sys.exit(1)

            graph.add_edge(i, int(j))

#już działa
if sys.argv[1] == "--generate":
    try:
        num_nodes = int(input("nodes> "))
        if num_nodes <0:
            raise ValueError
        saturation = int(input("saturation> "))
        if saturation <0:
            raise ValueError
    except:
        print("Niewłaściwe dane")
        sys.exit(1)
    graph=graphs.Graph(num_nodes)
    acyclic_graph=[[0] * num_nodes for _ in range(num_nodes)]
    max_num_of_ones=0
    list_of_ones=[]
    for i in range(0,num_nodes):
        max_num_of_ones+=i
    for _ in range(0,math.floor(max_num_of_ones*saturation/100)):
        list_of_ones.append(1)

    for i in range(0, num_nodes):
        for j in range(0,num_nodes):
            if i>=j:
                continue
            else:
                if len(list_of_ones) == 0:
                    break
                acyclic_graph[i][j]=list_of_ones.pop()
                graph.add_edge(i+1,j+1)

    
    print(acyclic_graph)
    print(max_num_of_ones)

representation = input("representation_type> ")

while(True):
    # graph = graphs.Graph(5)
    # graph.add_edge(1, 1)
    # graph.add_edge(1, 2)
    # graph.add_edge(2, 3)
    # graph.add_edge(3, 4)
    # graph.add_edge(4, 1)
    menu(representation)


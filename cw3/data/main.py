import graphs
import sys
import math

def printing_help():
    print("help\t\tshows this message")
    print("print\t\tasks user what graph representation should be printed and print it")
    print("find_edge\tfinds if edge between two vertices exits")
    print("BFS\t\tprints graph in breath-first-search way")
    print("DFS\t\tprints graph in depth-first-search way")
    print("Khan\t\tprints graph in topological sort using Khan algorithm")
    print("Tarjan\t\tprints graph in topological sort using Tarjan algorithm")
    print("export\t\texports graph to tikzpicture")
    print("exit\t\texits the program")


def menu(representation):
    action = input("\naction> ")
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
            try:
                source = int(input("from> "))
                destination = int(input("to> "))
                if (source or destination) <= 0:
                    raise ValueError
            except:
                print("Niewłaściwe dane")
                sys.exit(1)
            if graph.find_edge(source, destination, representation) == True:
                print(f'edge ({source}, {destination}) exists')
            else:
                print(f'edge ({source}, {destination}) does not exist')


        case "BFS":
            graph.search(find_min_incoming_edges(),representation, "BFS")
            
        case "DFS":
            graph.search(find_min_incoming_edges(),representation, "DFS")

        case "Khan":
            graph.topological_sort()

        case "Tarjan":
            pass

        case "export":
            string="\documentclass{article}\n\\usepackage{tikz}\n\\begin{document}\n"
            f=open("graph.tex", "w", encoding="utf-8")
            f.write(string)
            f.write(graph.export_graph())
            f.write("\n\end{document}")
            f.close()

        case "exit":
            sys.exit(1)

def find_min_incoming_edges():
    minimum = num_nodes
    num_incoming_edges=[]
    for _ in range(0,num_nodes):
        num_incoming_edges.append(0)
    for i in graph.successor_list:
        for x in i:
            if x!=0:
                num_incoming_edges[x-1] +=1
    for i in range(0, len(num_incoming_edges)):
        if num_incoming_edges[i] == 0 and graph.successor_list[i] == []:
            continue
        elif minimum>=num_incoming_edges[i]:
            minimum = num_incoming_edges[i]
    return num_incoming_edges.index(minimum) + 1

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
        if saturation <0 or saturation >100:
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

try:    
    representation = input("representation_type> ")
    if representation not in ["matrix", "list", "table"]:
        raise ValueError
except:
    print("Niewłaściwe dane")
    sys.exit(1)

while(True):
    menu(representation)


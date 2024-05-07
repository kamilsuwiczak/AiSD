import graphs
import sys

def menu():
    action = input("action> ")
    match action:
        case "help":
            print("help\t\tshows this message")
            print("print\t\tasks user what graph representation should be printed and print it")
            print("find_edge\tfinds if edge between two vertices exits")
            print("BFS\t\tprints graph in breath-first-search way")
            print("DFS\t\tprints graph in depth-first-search way")
            print("exit\t\texits the program")
        
        case "print":
            type_of_representation=input("type> ")
            match type_of_representation:
                case "matrix":
                    graph.print_matrix()
                case "list":
                    graph.print_successor_list()
                case "table":
                    pass

        case "find_edge":
            pass

        case "BFS":
            pass
        
        case "DFS":
            pass

        case "exit":
            sys.exit(1)

# jeszcze nie działa
if sys.argv[1] == "--user-provided":
    num_nodes = int(input("nodes> "))
    graph = graphs.Graph(num_nodes)
    for i in range(1, num_nodes+1):
        vertices = input(f'{i}> ').split()
        for j in vertices:
            graph.add_edge(i, int(j))



while(True):
    # graph = graphs.Graph(5)
    # graph.add_edge(1, 1)
    # graph.add_edge(1, 2)
    # graph.add_edge(2, 3)
    # graph.add_edge(3, 4)
    # graph.add_edge(4, 1)
    menu()


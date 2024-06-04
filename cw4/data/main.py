import graphs
import sys

def printing_help():
    print("help\t\tshows this message")
    print("print\t\tasks user what graph representation should be printed and print it")
    print("find_edge\tfinds if edge between two vertices exits")
    print("BFS\t\tprints graph in breath-first-search way")
    print("DFS\t\tprints graph in depth-first-search way")
    print("Khan\t\tprints graph in topological sort using Khan algorithm")
    print("Tarjan\t\tprints graph in topological sort using Tarjan algorithm")
    print("export\t\tdraws this graph in matplotlib")
    print("exit\t\texits the program")


def menu():
    action = input("\naction> ")
    match action:
        case "help":
            printing_help()

        case "export":
            graph.draw_graph()

        case "exit":
            sys.exit(1)


#saturation podajemy jako pełną liczbę np 70 a nie 0.7
if sys.argv[1] == "--hamilton":
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
    graph.generate_hamiltonian_graph(num_nodes, (saturation/100))




while(True):
    menu()


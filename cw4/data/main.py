import graphs
import sys

def printing_help():
    print("help\t\tshows this message")
    print("print\t\tprints the graph")
    print("export\t\tdraws this graph in matplotlib")
    print("exit\t\texits the program")


def menu():
    action = input("\naction> ")
    match action:
        case "help":
            printing_help()

        case "print":
            graph.print_graph()

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
    graph=graphs.Graph()
    graph.generate_hamiltonian_graph(num_nodes, (saturation/100))

if sys.argv[1] == "--non-hamilton":
    pass




while(True):
    menu()


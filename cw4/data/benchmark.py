from graphs import Graph
import os






def main():
    if os.path.exists("benchmark_results") == False:
        os.mkdir("benchmark_results")
    

    graph = Graph()
    graph.generate_hamiltonian_graph(1025, 0.3)
    graph.print_graph()

if __name__ == "__main__":
    main()

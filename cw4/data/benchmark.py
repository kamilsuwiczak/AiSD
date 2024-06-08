from graphs import Graph
import os
import sys
import time






def main():
    if os.path.exists("benchmark_results") == False:
        os.mkdir("benchmark_results")
    
    

    graph = Graph()

    file1 = open("benchmark_results/generating_hamiltonian_graph.csv", "w")
    file1.write("type_of_action, instance_size, time\n")
    
    file2 = open("benchmark_results/find_Euler_Hamilton.csv", "w")
    file2.write("type_of_action, instance_size, time\n")
    for i in range (0,2):
        start_time=time.time()
        graph.generate_hamiltonian_graph(2**i, 0.3)
        finish_time = time.time() - start_time
        file1.write(f"generating_hamiltonian_graph, {2**i}, {finish_time}\n")

        start_time1 = time.time()
        graph.find_eulerian_cycle()
        finish_time1 = time.time()-start_time1
        file2.write(f"finding_eulerian_cycle_in_hamiltonian_graph, {2**i}, {finish_time1}\n")

    file1.close()
    file2.close()
if __name__ == "__main__":
    main()

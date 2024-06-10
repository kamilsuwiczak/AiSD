import graphs
import os
import time
import sys

#nie wiem czemu ten benchmark tak dziwnie działa ale jakas chujnia sie zadziała przy non-hamilton graphs dlatego trzeba to odpalac z reki
def main():
    if os.path.exists("benchmark_results") == False:
        os.mkdir("benchmark_results")
    sys.setrecursionlimit(1000000000)

    graph = graphs.Graph()

    # file1 = open("benchmark_results/generating_hamiltonian_graph.csv", "w")
    # file1.write("type_of_action, instance_size, time\n")
    
    # file2 = open("benchmark_results/find_hamilton_cycle_Hamilton.csv", "w")
    # file2.write("type_of_action, instance_size, time\n")

    # file3 = open("benchmark_results/find_eulerian_cycle_Hamilton.csv", "w")
    # file3.write("type_of_action, instance_size, time\n")

    # for i in range (2,14):
    #     start_time=time.time()
    #     #mierzenie czasu generowanie grafow hamiltonowskich
    #     graph.generate_hamiltonian_graph(2**i, 0.3)
    #     finish_time = time.time() - start_time
    #     file1.write(f"generating_hamiltonian_graph, {2**i}, {finish_time}\n")

    #     #mierzenie czasu znajdowania cyklu hamiltona w grafie hamiltonowskim
    #     start_time = time.time()
    #     graph.find_hamiltonian_cycle()
    #     finish_time = time.time()-start_time
    #     file2.write(f"finding_hamiltonian_cycle_in_hamiltonian_graph, {2**i}, {finish_time}\n")

    #     #mierzenie czasu znajdowania cyklu eulera w grafie hamiltonowskim
    #     start_time = time.time()
    #     graph.find_eulerian_cycle()
    #     finish_time = time.time()-start_time
    #     file3.write(f"finding_eulerian_cycle_in_hamiltonian_graph, {2**i}, {finish_time}\n")


    # file1.close()
    # file2.close()
    # file3.close()

    file4 = open("benchmark_results/generating_non_hamiltonian_graph.csv", "a")
    # file4.write("type_of_action, instance_size, time\n")

    # file5 = open("benchmark_results/find_hamilton_cycle_non_Hamilton.csv", "w")
    # file5.write("type_of_action, instance_size, time\n")
    # file5.close()
    file5 = open("benchmark_results/find_hamilton_cycle_non_Hamilton.csv", "a")

    for i in range (16,17):
        start_time=time.time()
        #mierzenie czasu generowanie grafow nie-hamiltonowskich
        graph.generate_non_hamiltonian_graph(i)
        finish_time = time.time() - start_time
        file4.write(f"generating_non_hamiltonian_graph, {i}, {finish_time}\n")

        #mierzenie czasu znajdowania cyklu hamiltona w grafie niehamiltonowskim
        start_time = time.time()
        graph.find_hamiltonian_cycle()
        finish_time = time.time()-start_time
        file5.write(f"finding_hamiltonian_cycle_in_non_hamiltonian_graph, {i}, {finish_time}\n")

        
    file4.close()
    file5.close()

if __name__ == "__main__":
    main()

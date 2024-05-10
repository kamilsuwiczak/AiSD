import os
import sys
import trees
import time


def measure_time_of_creating_tree(tree_type, data_path, results_path):
    f1 = open(results_path, "a")
    measured_time=[]
    files = os.listdir(f"{data_path}")
    for i in files:
        tab=[]
        f2=open(f"{data_path}/{i}", "r")
        x = int(f2.readline())
        for _ in range(0, x):
            tab.append(int(f2.readline()))
        f2.close()
        if tree_type =="AVL":
            for _ in range(0,4):
                start_time = time.time()
                tree = trees.AVL(tab)
                finish_time = time.time()-start_time
                measured_time.append(finish_time)
                
            average_time = str(sum(measured_time)/len(measured_time)).replace(".", ",")
            f1.write(f"creating AVL\t{i}\t{x}\t{average_time}\n")
            measured_time.clear()
            tab.clear()

        elif tree_type == "BST":
            for _ in range(0,4):
                start_time = time.time()
                tree = trees.BST(tab)
                finish_time = time.time()-start_time
                measured_time.append(finish_time)
                
            average_time = str(sum(measured_time)/len(measured_time)).replace(".", ",")
            f1.write(f"creating BST\t{i}\t{x}\t{average_time}\n")
            measured_time.clear()
            tab.clear()
    f1.close()

def measure_time_of_finding_min_and_max_tree(tree_type, data_path, results_path):
    f1 = open(results_path, "a")
    measured_time=[]
    files = os.listdir(f"{data_path}")
    for i in files:
        tab=[]
        f2=open(f"{data_path}/{i}", "r")
        x = int(f2.readline())
        for _ in range(0, x):
            tab.append(int(f2.readline()))
        f2.close()
        if tree_type == "BST":
            for _ in range(0,4):
                tree = trees.BST(tab)
                start_time = time.time()
                min_element = tree.find_min()
                max_element = tree.find_max()
                finish_time=time.time()-start_time
                measured_time.append(finish_time)
            average_time = str(sum(measured_time)/len(measured_time)).replace(".", ",")
            f1.write(f"finding min max in BST\t{i}\t{x}\t{average_time}\n")
            measured_time.clear()
            tab.clear()
        elif tree_type == "AVL":
            for _ in range(0,4):
                tree = trees.AVL(tab)
                start_time = time.time()
                min_element = tree.find_min()
                max_element = tree.find_max()
                finish_time=time.time()-start_time
                measured_time.append(finish_time)
            average_time = str(sum(measured_time)/len(measured_time)).replace(".", ",")
            f1.write(f"finding min max in AVL\t{i}\t{x}\t{average_time}\n")
            measured_time.clear()
            tab.clear()
    f1.close()


def measure_time_of_printing_degenerated_tree_inorder(tree_type, data_path, results_path):
    f1 = open(results_path, "a")
    measured_time=[]
    files = os.listdir(f"{data_path}")
    for i in files:
        tab=[]
        f2=open(f"{data_path}/{i}", "r")
        x = int(f2.readline())
        for j in range(0, x):
            tab.append(int(f2.readline()))
        f2.close()
        if tree_type == "BST":
            for _ in range(0,4):
                tree = trees.BST(tab)
                start_time = time.time()
                print(tree.print_inorder())
                finish_time = time.time()-start_time
                measured_time.append(finish_time)
            average_time = str(sum(measured_time)/len(measured_time)).replace(".", ",")
            measured_time.clear()
            f1.write(f"printing degenerated BST in-order\t{i}\t{x}\t{average_time}\n")
            tab.clear()
        elif tree_type == "AVL":
            for _ in range(0,4):
                tree = trees.AVL(tab)
                start_time = time.time()
                print(tree.print_inorder())
                finish_time =time.time()-start_time
                measured_time.append(finish_time)
            average_time = str(sum(measured_time)/len(measured_time)).replace(".", ",")
            measured_time.clear()
            f1.write(f"printing degenerated AVL in-order\t{i}\t{x}\t{average_time}\n")
            tab.clear()
    f1.close()

def measuring_time_of_rebelancing_BST(data_path, results_path):
    f1 = open(results_path, "a")
    measured_time=[]
    files = os.listdir(f"{data_path}")
    for i in files:
        tab=[]
        f2=open(f"{data_path}/{i}", "r")
        x = int(f2.readline())
        for j in range(0, x):
            tab.append(int(f2.readline()))
        f2.close()
        for _ in range(0,4):
            tree = trees.BST(tab)
            start_time = time.time()
            tree.balanceDSW()
            finish_time = time.time()-start_time
            measured_time.append(finish_time)
        average_time = str(sum(measured_time)/len(measured_time)).replace(".", ",")
        measured_time.clear()
        f1.write(f"printing degenerated BST in-order\t{i}\t{x}\t{average_time}\n")
        tab.clear()
    f1.close()



def main():
    tree_data_degenerated= "benchmark_data/degenerated_trees"
    tree_data_random = "benchmark_data/random"
    results_path = "benchmark_results/results.txt"
    if os.path.exists("benchmark_results") == False:
        os.mkdir("benchmark_results")
    if os.path.exists(results_path) == False:
        file=open(results_path, "x")
        file.write("Action\tname_of_file\tnumber_of_elements\ttime\n")
        file.close()
    else:
        os.remove(results_path)
        file=open(results_path, "x")
        file.write("Action\tname_of_file\tnumber_of_elements\ttime\n")
        file.close()
    sys.setrecursionlimit(1000000)
    
    measure_time_of_creating_tree("AVL", tree_data_degenerated, results_path)
    measure_time_of_creating_tree("AVL", tree_data_random, results_path)
    measure_time_of_creating_tree("BST", tree_data_degenerated, results_path)
    measure_time_of_creating_tree("BST", tree_data_random, results_path)
    measure_time_of_finding_min_and_max_tree("BST", tree_data_random, results_path)
    measure_time_of_finding_min_and_max_tree("BST", tree_data_degenerated, results_path)
    measure_time_of_finding_min_and_max_tree("AVL", tree_data_random, results_path)
    measure_time_of_finding_min_and_max_tree("BST", tree_data_degenerated, results_path)
    

    

if __name__ == '__main__':
    main()

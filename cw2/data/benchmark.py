import os
import trees
import time


def measure_time_of_creating_tree(tree_type, data_path):
    f1 = open("benchmark_results/results.txt", "a")
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
                measured_time.append(time.time()-start_time)
                
            average_time = str(sum(measured_time)/len(measured_time)).replace(".", ",")
            f1.write(f"creating AVL\t{i}\t{x}\t{average_time}\n")
            tab.clear()

        elif tree_type == "BST":
            for _ in range(0,4):
                start_time = time.time()
                tree = trees.BST(tab)
                measured_time.append(time.time()-start_time)
                
            average_time = str(sum(measured_time)/len(measured_time)).replace(".", ",")
            f1.write(f"creating BST\t{i}\t{x}\t{average_time}\n")
            tab.clear()
    f1.close()

def measure_time_of_finding_min_and_max_tree(tree_type, data_path):
    f1 = open("benchmark_results/results.txt", "a")
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
                measured_time.append(time.time()-start_time)
            
            average_time = str(sum(measured_time)/len(measured_time)).replace(".", ",")
            f1.write(f"finding min max in BST\t{i}\t{x}\t{average_time}\n")
            tab.clear()
        elif tree_type == "AVL":
            for _ in range(0,4):
                tree = trees.AVL(tab)
                start_time = time.time()
                min_element = tree.find_min()
                max_element = tree.find_max()
                measured_time.append(time.time()-start_time)
            average_time = str(sum(measured_time)/len(measured_time)).replace(".", ",")
            f1.write(f"finding min max in AVL\t{i}\t{x}\t{average_time}\n")
            tab.clear()

def measure_time_of_printing_degenerated_tree_inorder(tree_type, data_path):
    f1 = open("benchmark_results/results.txt", "a")
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
            for k in range(0,4):
                tree = trees.BST(tab)
                start_time = time.time()
                print(tree.print_inorder())
                measured_time.append(time.time()-start_time)
            average_time = str(sum(measured_time)/len(measured_time)).replace(".", ",")
            f1.write(f"printing degenerated BST in-order\t{i}\t{x}\t{average_time}\n")
            tab.clear()
        if tree_type == "AVL":
            for k in range(0,4):
                tree = trees.AVL(tab)
                start_time = time.time()
                print(tree.print_inorder())
                measured_time.append(time.time()-start_time)
            average_time = str(sum(measured_time)/len(measured_time)).replace(".", ",")
            f1.write(f"printing degenerated AVL in-order\t{i}\t{x}\t{average_time}\n")
            tab.clear()

def main():
    if os.path.exists("benchmark_results") == False:
        os.mkdir("benchmark_results")
    if os.path.exists("benchmark_results/results.txt") == False:
        file=open("benchmark_results/results.txt", "x")
        file.write("Action\tname_of_file\tnumber_of_elements\ttime\n")
        file.close()
    else:
        os.remove("benchmark_results/results.txt")
        file=open("benchmark_results/results.txt", "x")
        file.write("Action\tname_of_file\tnumber_of_elements\ttime\n")
        file.close()
    measure_time_of_creating_tree("AVL", "benchmark_data/random")
    measure_time_of_creating_tree("BST", "benchmark_data/random")
    measure_time_of_finding_min_and_max_tree("BST", "benchmark_data/random")
    measure_time_of_finding_min_and_max_tree("AVL", "benchmark_data/random")
    measure_time_of_printing_degenerated_tree_inorder("AVL", "benchmark_data/degenerated_trees")
    measure_time_of_printing_degenerated_tree_inorder("BST", "benchmark_data/degenerated_trees")


if __name__ == '__main__':
    main()
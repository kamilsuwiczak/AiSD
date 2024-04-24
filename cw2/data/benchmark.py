import sys
import os
import trees
import time


def measure_time_of_creating_AVL():
    f1 = open("benchmark_results/results.txt", "a")
    files = os.listdir("benchmark_data/random")
    for i in files:
        tab=[]
        f2=open(f"benchmark_data/random/{i}", "r")
        x = int(f2.readline())
        for j in range(0, x):
            tab.append(int(f2.readline()))
        f2.close()

        for k in range(0,4):
            start_time = time.time()
            tree = trees.AVL(tab)
            finish_time=time.time()-start_time
            finish_time = str(finish_time).replace(".", ",")
            f1.write(f"creating AVL\t{i}\t{x}\t{finish_time}\n")
        tab.clear()
    f1.close()

def measure_time_of_creating_BST():
    f1 = open("benchmark_results/results.txt", "a")
    files = os.listdir("benchmark_data/degenerated_trees")
    for i in files:
        tab=[]
        f2=open(f"benchmark_data/degenerated_trees/{i}", "r")
        x = int(f2.readline())
        for j in range(0, x):
            tab.append(int(f2.readline()))
        f2.close()

        for k in range(0,4):
            start_time = time.time()
            tree = trees.BST(tab)
            finish_time=time.time()-start_time
            finish_time = str(finish_time).replace(".", ",")
            f1.write(f"creating BST\t{i}\t{x}\t{finish_time}\n")
        tab.clear()
    f1.close()

def measure_time_of_finding_min_and_max_BST():
    f1 = open("benchmark_results/results.txt", "a")
    
    files = os.listdir("benchmark_data/random")
    for i in files:
        tab=[]
        f2=open(f"benchmark_data/random/{i}", "r")
        x = int(f2.readline())
        for j in range(0, x):
            tab.append(int(f2.readline()))
        f2.close()

        for k in range(0,4):
            tree = trees.BST(tab)
            start_time = time.time()
            min_element = tree.find_min()
            max_element = tree.find_max()
            finish_time=time.time()-start_time
            finish_time = str(finish_time).replace(".", ",")
            f1.write(f"finding min max in BST\t{i}\t{x}\t{finish_time}\n")
        tab.clear()
    f1.close()


def measure_time_of_finding_min_and_max_AVL():
    f1 = open("benchmark_results/results.txt", "a")
    files = os.listdir("benchmark_data/random")
    for i in files:
        tab=[]
        f2=open(f"benchmark_data/random/{i}", "r")
        x = int(f2.readline())
        for j in range(0, x):
            tab.append(int(f2.readline()))
        f2.close()

        for k in range(0,4):
            tree = trees.AVL(tab)
            start_time = time.time()
            min_element = tree.find_min()
            max_element = tree.find_max()
            finish_time=time.time()-start_time
            finish_time = str(finish_time).replace(".", ",")
            f1.write(f"finding min max in AVL\t{i}\t{x}\t{finish_time}\n")
        tab.clear()
    f1.close()

def measure_time_of_printing_degenerated_BST_inorder():
    f1 = open("benchmark_results/results.txt", "a")
    files = os.listdir("benchmark_data/degenerated_trees")
    for i in files:
        tab=[]
        f2=open(f"benchmark_data/degenerated_trees/{i}", "r")
        x = int(f2.readline())
        for j in range(0, x):
            tab.append(int(f2.readline()))
        f2.close()
        for k in range(0,4):
            tree = trees.AVL(tab)
            start_time = time.time()
            print(tree.print_inorder())
            finish_time=time.time()-start_time
            finish_time = str(finish_time).replace(".", ",")
            f1.write(f"printing degenerated BST in-order\t{i}\t{x}\t{finish_time}\n")
        tab.clear()
    f1.close()



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
    # print(printing_from_files())
    # test_print()
    measure_time_of_creating_AVL()
    measure_time_of_creating_BST()
    measure_time_of_finding_min_and_max_BST()
    measure_time_of_finding_min_and_max_AVL()
    measure_time_of_printing_degenerated_BST_inorder()
    


if __name__ == '__main__':
    main()
import sys
import os
import trees
import time


def measure_time_of_creating_AVL():
    f1 = open("benchmark_results/results.txt", "a")
    f1.write("Action, number_of_elements, time\n")
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
            f1.write(f"creating AVL, {i}, {finish_time}\n")
        tab.clear()
    f1.close()

def measure_time_of_creating_BST():
    f1 = open("benchmark_results/results.txt", "a")
    f1.write("Action, number_of_elements, time\n")
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
            tree = trees.BST(tab)
            finish_time=time.time()-start_time
            finish_time = str(finish_time).replace(".", ",")
            f1.write(f"creating BST, {i}, {finish_time}\n")
        tab.clear()
    f1.close()

def test_print():
    f= open("benchmark_data/random/4_random_elements.txt")
    tab=[]
    x = int(f.readline())
    for j in range(0, x):
        tab.append(int(f.readline()))

    f.close()
    start_time = time.time()
    tree = trees.AVL(tab)
    print(time.time()-start_time)




def main():
    if os.path.exists("benchmark_results") == False:
        os.mkdir("benchmark_results")
    if os.path.exists("benchmark_results/results.txt") == False:
        file=open("benchmark_results/results.txt", "x")
        file.close()
    # print(printing_from_files())
    # test_print()
    measure_time_of_creating_AVL()
    measure_time_of_creating_BST()
    # files = os.listdir("benchmark_data/random")
    # dx = trees.AVL([8,2,5,14,10,12,13,6,9,1,4])
    # start_time = time.time()
    # print(dx.print())
    # print(time.time()-start_time)
    # print(files)



if __name__ == '__main__':
    main()
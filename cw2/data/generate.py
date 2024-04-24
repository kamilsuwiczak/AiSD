import random
import os

def generate_random_data(n):
    filename = f"benchmark_data/random/{2**n}_random_elements.txt" 
    print(filename)
    f = open(filename, "w")
    f.write(str(2**n)+"\n")
    for i in range(0,2**n):
        f.write(str(random.randint(1, 2**n))+ "\n")
    f.close()


def generate_degenerated_trees_data(n):
    filename = f"benchmark_data/degenerated_trees/{2**n}_degenerated_tree_elements.txt" 
    print(filename)
    f = open(filename, "w")
    f.write(str(2**n)+"\n")
    for i in range(2**n,0,-1):
        f.write(str(i)+ "\n")
    f.close()



def main():
    if os.path.exists("benchmark_data/random") == False:
        os.mkdir("benchmark_data/random")

    if os.path.exists("benchmark_data/degenerated_trees") == False:
        os.mkdir("benchmark_data/degenerated_trees")
        
    for i in range(1,16):
        # generate_random_data(i)
        generate_degenerated_trees_data(i)


if __name__ == '__main__':
    main()
import random
import os

def generate_data(n):
    filename = f"benchmark_data/random/{2**n}_random_elements.txt" 
    print(filename)
    f = open(filename, "w")
    f.write(str(2**n)+"\n")
    for i in range(0,2**n):
        f.write(str(random.randint(1, 2**n))+ "\n")
        
    f.close()

def main():
    if os.path.exists("benchmark_data/random") == False:
        os.mkdir("benchmark_data/random")
    for i in range(1,16):
        generate_data(i)


if __name__ == '__main__':
    main()
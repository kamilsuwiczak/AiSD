import sys
import random
import os

def generate_data(n):
    filename = str(2**n) + "_random_elements.txt" 
    print(filename)
    f = open(filename, "w")
    f.write(str(2**n)+"\n")
    for i in range(0,2**n):
        f.write(str(random.randint(1, 2**n))+ "\n")
        
    f.close()



def main():
    for i in range(0,16):
        generate_data(i)


if __name__ == '__main__':
    main()
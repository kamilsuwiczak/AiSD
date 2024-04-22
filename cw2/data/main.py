import trees
import sys

x= True
y=[]
#Obsługa BST podawanego jako python3 main.py --tree BST 16 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17, gdzie 16 to liczba węzłów
if sys.argv[1] =="--tree" and sys.argv[2] == "BST" and len(sys.argv)>3:
    for i in range (0, int(sys.argv[3])):
        y.append(int(sys.argv[i+4]))

z=trees.BST(y)
print(z.print())

# while x:
#     print('''wybierz opcje: 
#           1. Wprowadz drzewo\n
#           2. Zakończ \n''')
#     y=input(">>>")
#     if int(y) == 2:
#         x= False



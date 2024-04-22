import trees
import sys

x= True
y=[]
action =""

#Obsługa BST podawanego jako python3 main.py --tree BST 16 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17, gdzie 16 to liczba węzłów
if sys.argv[1] =="--tree" and sys.argv[2] == "BST" and len(sys.argv)>3:
    for i in range (0, int(sys.argv[3])):
        y.append(int(sys.argv[i+4]))
# Obsługa BST podawanego do programu jako node> i insert>
elif sys.argv[1] =="--tree" and sys.argv[2] == "BST" and len(sys.argv)<=3:
    x=input("nodes> ")
    a=input("insert >")
    for i in range(0, len(a)):
        if a[i]==" ":
            continue
        y.append(int(a[i]))
# print(len(sys.argv))
z=trees.BST(y)
# print(z.print())

#menu 
while(x):
    action = input("action> ")
    match action:
        case "help":
            print("help         Show this message")
            print("print        Print the tree using in-order, pre-order, post-order")
            print("remove       Remove elements of the tree")
            print("delete       Delete the whole tree")
            print("export       Export the tree to tickzpicture")
            print("rebalance    Rebalance the tree")
            print("exit         Exits the program (the same as ctrl + D)")
        case  "print":
            print(z.print())
        case "remove":
            action = input("remove> ")
        case "export":
            pass
        case "rebalance":
            pass
        case "exit":
            x= False
        
    

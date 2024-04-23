import trees
import sys

x= True
bst_data=[]
action =""

#Obsługa BST podawanego jako python3 main.py --tree BST 16 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17, gdzie 16 to liczba węzłów
if sys.argv[1] =="--tree" and sys.argv[2] == "BST" and len(sys.argv)>3:
    for i in range (0, int(sys.argv[3])):
        bst_data.append(int(sys.argv[i+4]))
    z=trees.BST(bst_data)
# Obsługa BST podawanego do programu jako node> i insert>
elif sys.argv[1] =="--tree" and sys.argv[2] == "BST" and len(sys.argv)<=3:
    nodes=input("nodes> ")
    a=input("insert >")
    for i in range(0, len(a)):
        if a[i]==" ":
            continue
        bst_data.append(int(a[i]))
    z=trees.BST(bst_data)
#obsługa AVL podawanego do programu jako python3 main.py --tree AVL 11 8 2 5 14 10 12 13 6 9 1 4, gdzie 11 to liczba węzłów
elif sys.argv[1] =="--tree" and sys.argv[2] == "AVL" and len(sys.argv)>3:
    for i in range (0, int(sys.argv[3])):
        bst_data.append(int(sys.argv[i+4]))
    z=trees.AVL(bst_data)
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
            print("findMinMax   Finding minimum and maximum in tree")
            print("exit         Exits the program (the same as ctrl + D)")

        case  "print":
            tab = z.print()
            print("pre-order: ", tab[0])
            print("In-order: ", tab[1])
            print("post-order: ", tab[2])

        case "remove":
            tab=[]
            tmp=""
            nodes_to_remove = input("remove> ")
            for i in range (0, len(nodes_to_remove)):
                if nodes_to_remove[i] != " ":
                    tmp = tmp+nodes_to_remove[i]
                if nodes_to_remove[i] == " " or i == len(nodes_to_remove)-1:
                    tab.append(tmp)
                    tmp = ""
            for i in tab:
                z.delete(int(i))

        case "delete":
            z.del_all()
            print("Tree has been deleted")

        case "export":
            pass

        case "rebalance":
            pass
        case "findMinMax":
            print("Min: ", z.find_min())
            print("Max", z.find_max())
        case "exit":
            x= False
        
    

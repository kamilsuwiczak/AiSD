import trees
import sys

tree_data=[]
if sys.argv[1] =="--tree" and sys.argv[2] == "BST" and len(sys.argv)==3:
    print(len(sys.argv))
    x=input()
    x= x.split()
    for i in range (0, int(x.pop(0))):
        tree_data.append(int(x.pop(0)))
    z=trees.BST(tree_data)
    for i in x:
        action = i
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
                pass

elif sys.argv[1] =="--tree" and sys.argv[2] == "BST" and sys.argv[3]=="hand":
    nodes=input("nodes> ")
    a=input("insert >")
    for i in range(0, len(a)):
        if a[i]==" ":
            continue
        tree_data.append(int(a[i]))
    z=trees.BST(tree_data)
    
    while(True):
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
                break


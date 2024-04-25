import trees
import sys

tree_data=[]
# program odpala się poprzez python3 main.py --tree BST <<< "2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 actions"
if sys.argv[1] =="--tree" and sys.argv[2] == "BST" and len(sys.argv)==3:
    # print(len(sys.argv))
    x=input()
    print(x)
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
                tab = z.print_tree()
                print("pre-order: ", *tab[0])
                print("In-order: ", *tab[1])
                print("post-order: ", *tab[2])

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
                string="\documentclass{standalone}\n\\usepackage{tikz}\n\\usepackage{tikz-qtree}\n\\begin{document}\n"
                f=open("bst_tree.tex", "w", encoding="utf-8")
                f.write(string)
                f.write(z.generate_tree_in_tikz())
                f.write("\n\end{document}")
                f.close()

            case "rebalance":
                pass
            case "findMinMax":
                print("Min: ", z.find_min())
                print("Max", z.find_max())
            case "exit":
                pass
# program odpala się poprzez python3 main.py --tree AVL <<< "2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 actions"
elif sys.argv[1] =="--tree" and sys.argv[2] == "AVL" and len(sys.argv)==3:
    # print(len(sys.argv))
    x=input()
    x= x.split()
    for i in range (0, int(x.pop(0))):
        tree_data.append(int(x.pop(0)))
    z=trees.AVL(tree_data)
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
                tab = z.print_tree()
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
                string="\documentclass{standalone}\n\\usepackage{tikz}\n\\usepackage{tikz-qtree}\n\\begin{document}\n"
                f=open("avl_tree.tex", "w", encoding="utf-8")
                f.write(string)
                f.write(z.generate_tree_in_tikz())
                f.write("\n\end{document}")
                f.close()
                pass

            case "rebalance":
                z.balanceDSW()
            case "findMinMax":
                print("Min: ", z.find_min())
                print("Max", z.find_max())
            case "exit":
                pass

# program odpala się poprzez python3 main.py --tree BST hand, a następnie można w programie podać ilość nodów 
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
                string="\documentclass{standalone}\n\\usepackage{tikz}\n\\usepackage{tikz-qtree}\n\\begin{document}\n"
                f=open("bst_tree.tex", "w", encoding="utf-8")
                f.write(string)
                f.write(z.generate_tree_in_tikz())
                f.write("\n\end{document}")
                f.close()
                

            case "rebalance":
                pass
            case "findMinMax":
                print("Min: ", z.find_min())
                print("Max", z.find_max())
            case "exit":
                break

# program odpala się poprzez python3 main.py --tree AVL hand, a następnie można w programie podać ilość nodów 
elif sys.argv[1] =="--tree" and sys.argv[2] == "AVL" and sys.argv[3]=="hand":
    nodes=input("nodes> ")
    a=input("insert >")
    for i in range(0, len(a)):
        if a[i]==" ":
            continue
        tree_data.append(int(a[i]))
    z=trees.AVL(tree_data)
    
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
                tab = z.print_tree()
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
                string="\documentclass{standalone}\n\\usepackage{tikz}\n\\usepackage{tikz-qtree}\n\\begin{document}\n"
                f=open("avl_tree.tex", "w", encoding="utf-8")
                f.write(string)
                f.write(z.generate_tree_in_tikz())
                f.write("\n\end{document}")
                f.close()
                
            case "rebalance":
                z.balanceDSW()
            case "findMinMax":
                print("Min: ", z.find_min())
                print("Max", z.find_max())
            case "exit":
                break


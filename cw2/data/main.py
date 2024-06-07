import trees
import sys


def menu(action):
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
                tab = tree.print_tree()
                print("pre-order: ", *tab[0])
                print("In-order: ", *tab[1])
                print("post-order: ", *tab[2])
            
            case "remove":
                try:
                    nodes_to_remove = input("remove> ").split()
                    nodes_to_remove = [int(i) for i in nodes_to_remove]
                    for node in nodes_to_remove:
                        if node < 0:
                            raise ValueError
                        tree.delete(node)
                except:
                    print("Niewłaściwe dane")
                    sys.exit(1)
            
            case "delete":
                tree.del_all()
                print("Tree has been deleted")

            case "export":
                string="\documentclass{standalone}\n\\usepackage{tikz}\n\\usepackage{tikz-qtree}\n\\begin{document}\n"
                f=open("bst_tree.tex", "w", encoding="utf-8")
                f.write(string)
                f.write(tree.generate_tree_in_tikz())
                f.write("\n\end{document}")
                f.close()

            case "rebalance":
                tree.balanceDSW()
            case "findMinMax":
                print("Min: ", tree.find_min())
                print("Max", tree.find_max())
            case _:
                print("Niewłaściwa komenda")

tree_data = []
# program odpala się poprzez python3 main.py --tree [AVL/BST] <<< "[liczba node'ow] [node] [node].....[node] actions"
tree_type = sys.argv[2]

if sys.argv[1] == "--tree" and (tree_type == "AVL" or tree_type == "BST")  and len(sys.argv) == 3:

    input_string=input()
    print(input_string)
    input_string= input_string.split()
    
    try:
        arg = int(input_string.pop(0))
        for i in range (0, arg):
                if arg < 0:
                    raise ValueError 
                arg = int(input_string.pop(0))
                tree_data.append(arg)

    except:
        print("Niewłaściwe dane")
        sys.exit(1)
    if tree_type == "BST":
        tree=trees.BST(tree_data)
    else:
        tree =  trees.AVL(tree_data)
    for i in input_string:
        action = i
        menu(action)
        
# program odpala się poprzez python3 main.py --tree [AVL/BST] hand, a następnie można w programie podać ilość nodów 
elif sys.argv[1] =="--tree" and (tree_type == "AVL" or tree_type == "BST")  and sys.argv[3] == "hand":
    try:
        nodes=int(input("nodes > "))
        if nodes < 0:
            raise ValueError 
        for _ in range(nodes):
            if nodes < 0:
                raise ValueError
            tree_data.append(int(input("insert > ")))
        if tree_type == "BST":
            tree=trees.BST(tree_data)
        else:
            tree =  trees.AVL(tree_data)
    except:
        print("Niewłaściwe dane")
        sys.exit(1)
    
    while True: 
        action = input("action> ")
        if action == "exit":
            break
        menu(action)
    


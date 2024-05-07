import graphs

def menu():
    action = input("action> ")
    match action:
        case "help":
            print("help\tshows this message")
            print("print\tasks user what graph representation should be printed and print it")
        
        case "print":
            type_of_representation=input("type> ")
            match type_of_representation:
                case "matrix":
                    pass
                case "list":
                    pass
                case "table":
                    pass
                



menu()
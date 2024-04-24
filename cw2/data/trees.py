import sys

class Node:
    def __init__(self,key):
        self.key = key 
        self.left = None
        self.right = None

class BST:
    def __init__(self,data):
        self.root = None
        for i in data:
            self.insert(i)
    
    def insert(self, key):
        new = Node(key)     
        if self.root is None:
            self.root = new
            return
        
        current = self.root
        while True:
            
            if key < current.key:       # lecimy na lewo az nie znajdziemy miejsca
                if current.left is None:
                    current.left = new
                    return
                current = current.left
           
            elif key > current.key:     # to samo ale na prawo
                if current.right is None:
                    current.right = new
                    return
                current = current.right
            
            else:   #w przypadku duplikatow nic nie robimy
                return
    def generate_tree_in_tikz(self):
        return "\\Tree " + self._generate_tikz(self.root)

    def _generate_tikz(self, node):
        if node is None:
            return ""
        left_str = self._generate_tikz(node.left)
        right_str = self._generate_tikz(node.right)
        if left_str or right_str:
            return f"[.{node.key} {left_str} {right_str} ]"
        else:
            return f"[.{node.key} ]"
        
    def print(self):
        preorder = []
        inorder = []
        postorder = []

        self.inorder_traversal(self.root, inorder)
        self.preorder_traversal(self.root,preorder)
        self.postorder_traversal(self.root,postorder)
        return preorder,inorder,postorder
    
    def print_inorder(self):
        inorder=[]
        self.inorder_traversal(self.root, inorder)
        return inorder

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.key)
            self.inorder_traversal(node.right, result)
    
    def preorder_traversal(self, node, result):
        if node:
            result.append(node.key)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)

    def postorder_traversal(self, node, result):
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.key)
    
    def find_min(self):
        if not self.root:
            return
        current = self.root
        while current.left is not None:
            current = current.left
        return current.key
    
    def find_max(self):
        if not self.root:
            return
        current = self.root
        while current.right is not None:
            current = current.right
        return current.key
    

    def delete(self, key, node=Node):
        if node == Node:   
            node = self.root
        if node is None:
            return node

        if key < node.key:                          #szukamy wartosci w drzewie
            node.left = self.delete(key, node.left) 
        elif key > node.key:
            node.right = self.delete(key, node.right)
        else:                       
            if node.left is None:   #przypadek 0 lub 1 potomka
                return node.right   
            elif node.right is None:
                return node.left

            current = node.right            
            while current.left is not None:
                current = current.left
    
            node.key = current.key
            node.right = self.delete(current.key, node.right)

        return node
    
    def del_all(self, node=Node):
        if node == Node:
            node = self.root
        if node:
            self.del_all(node.left)
            self.del_all(node.right)
            node.left = None
            node.right = None
            node.key = None

class AVLNode(Node):
    def __init__(self,key):
        super().__init__(key)
        self.height = 1

class AVL(BST):
    def __init__(self, data):
        super().__init__(data)
        self.root = self.build_avl_tree(sorted(data))
        
    def build_avl_tree(self, data):
            if not data:
                return None
            mid = len(data) // 2
            root = AVLNode(data[mid])
            root.left = self.build_avl_tree(data[:mid])
            root.right = self.build_avl_tree(data[mid+1:])
            self.updateHeight(root)
            return root
   
    def getBalance(self, node):
        if not node:
            return 0
        return node.left.height - node.right.height

    def updateHeight(self, node):
        node.height = 1 + max(node.left.height if node.left else 0, node.right.height if node.right else 0)

    def rightRotate(self, rotator):
        pivot = rotator.left
        temp = pivot.right

        pivot.right = rotator
        rotator.left = temp

        self.updateHeight(rotator)
        self.updateHeight(pivot)

        return pivot

    def leftRotate(self, rotator):
        pivot = rotator.right
        temp = pivot.left

        pivot.left = rotator
        rotator.right = temp

        self.updateHeight(rotator)
        self.updateHeight(pivot)

        return pivot

    
    
def main():
    xd = BST([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
    xx=BST([10,9,8,7,6,5,4,3,2,1])
    dx = BST([8,2,5,14,10,12,13,6,9,1,4])
    f= open("bst_tikz.tex", "w")
    f.write(dx.generate_tikz())
    f.close()
    

    print(xd.print())
    # print(dx.print())
    # print(xx.print())
    print(xd.print_inorder())

if __name__ == '__main__':
    main()




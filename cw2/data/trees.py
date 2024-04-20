import sys

class Node:
    def __init__(self,key):
        self.key = key 
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
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
        
    def print(self):
        preorder = []
        inorder = []
        postorder = []

        self.inorder_traversal(self.root, inorder)
        self.preorder_traversal(self.root,preorder)
        self.postorder_traversal(self.root,postorder)
        return preorder,inorder,postorder

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
    def __init__(self):
        super().__init__()
        self.height = 1

class AVL(BST):
    def __init__(self, data):
        super().__init__()
        
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
    xd = BST()

    xd.insert(2)
    xd.insert(5)
    xd.insert(10)
    xd.insert(12)
    xd.insert(13)
    xd.insert(6)
    xd.insert(9)
    print(xd.print())
    xd.del_all()
    print(xd.print())

if __name__ == '__main__':
    main()




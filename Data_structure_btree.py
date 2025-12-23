class BinaryNode:    
    def __init__(self, d):
        self.Lchild = None
        self.data = d
        self.Rchild = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insLeft(self, d):
        if self.root is None:
            self.root = BinaryNode(d)
        else:
            temp = self.root 
            while temp.Lchild:
                temp = temp.Lchild
            temp.Lchild = BinaryNode(d)

    def insRight(self, d):
        if self.root is None:
            self.root = BinaryNode(d)
        else:
            temp = self.root
            while temp.Rchild:
                temp = temp.Rchild
            temp.Rchild = BinaryNode(d)

    def displayNLR(self):
        self.showNLR(self.root)
    
    def showNLR(self, root):
        if root:
            print(root.data, end=" ")
            self.showNLR(root.Lchild)
            self.showNLR(root.Rchild)
    
    def displayLNR(self):
        self.showLNR(self.root)
    
    def showLNR(self, root):
        if root:
            self.showLNR(root.Lchild)
            print(root.data, end=" ")
            self.showLNR(root.Rchild)
    
    def displayLRN(self):
        self.showLRN(self.root)
    
    def showLRN(self, root):
        if root:
            self.showLRN(root.Lchild)
            self.showLRN(root.Rchild)
            print(root.data, end=" ")

    def levelOrder(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        
        while queue:
            k = queue.pop(0)
            print(k.data, end=" ") 
            if k.Lchild:
                queue.append(k.Lchild)  
            if k.Rchild:
                queue.append(k.Rchild)

    def insAfterL(self, x, d):
        self.pinsAfterL(self.root, x, d)
    def pinsAfterL(self, node, x, d):
        if node:
            if node.data == x:
                temp = node.Lchild
                node.Lchild = BinaryNode(d)
                node.Lchild.Lchild = temp
            self.pinsAfterL(node.Lchild, x, d)
            self.pinsAfterL(node.Rchild, x, d)

    def insAfterR(self, x, d):
        self.pinsAfterR(self.root, x, d)
    def pinsAfterR(self, node, x, d):
        if node:
            if node.data == x:
                temp = node.Rchild
                node.Rchild = BinaryNode(d)
                node.Rchild.Rchild = temp
            self.pinsAfterR(node.Lchild, x, d)
            self.pinsAfterR(node.Rchild, x, d)

    def delLeft(self):
        if self.root is None:
            print("empty")
            return
        if self.root.Lchild is None:
            temp = self.root.Rchild
            del self.root
            self.root = temp
            return
        temp = self.root
        while temp.Lchild and temp.Lchild.Lchild:
            temp = temp.Lchild
        if temp.Lchild:
            temp1 = temp.Lchild
            temp.Lchild = None
            del temp1

    def delRight(self):
        if self.root is None:
            print("empty")
            return   
        if self.root.Rchild is None:
            temp = self.root.Lchild
            del self.root
            self.root = temp
            return
        temp = self.root
        while temp.Rchild and temp.Rchild.Rchild:
            temp = temp.Rchild
        if temp.Rchild:
            temp1 = temp.Rchild
            temp.Rchild = None
            del temp1

    def delete_x(self, x):
        if self.root is None:
            print('empty')
            return None
        else:
            self.pdelete(self.root, x)
    def pdelete(self, node, x):
        if node is not None:
            if node.Lchild:
                if node.Lchild.data == x:
                    del node.Lchild
                    node.Lchild = None
                    return
                self.pdelete(node.Lchild, x)

            if node.Rchild:
                if node.Rchild.data == x:
                    del node.Rchild
                    node.Rchild = None
                    return
                self.pdelete(node.Rchild, x)

            if node.data == x:
                node = None
                return

if __name__ == "__main__":
    tree = BinaryTree()
    tree.insLeft(10)
    tree.insLeft(5)
    tree.insRight(15)
    tree.root.Lchild.Lchild = BinaryNode(3)
    tree.root.Lchild.Rchild = BinaryNode(7)

    print("Level Order Traversal:")
    tree.levelOrder()
    print()

    tree.insAfterL(5, 6)
    print("After inserting 6 as left child of 5:")
    tree.levelOrder()
    print()

    tree.insAfterR(5, 8)
    print("After inserting 8 as right child of 5:")
    tree.levelOrder()
    print()

    tree.delete_x(5)
    print("After deleting node with value 5:")
    tree.levelOrder()
    print()

    tree.delLeft()
    print("After deleting left child:")
    tree.levelOrder()
    print()

    tree.delRight()
    print("After deleting right child:")
    tree.levelOrder()
    print()

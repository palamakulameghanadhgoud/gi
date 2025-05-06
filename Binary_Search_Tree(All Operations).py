class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while temp:
                parent = temp
                if data < temp.data:
                    temp = temp.lchild
                else:
                    temp = temp.rchild
            if data < parent.data:
                parent.lchild = new_node
            else:
                parent.rchild = new_node
    def inorder(self, t):
        if t:
            self.inorder(t.lchild)
            print(t.data, end=" ")
            self.inorder(t.rchild)
    def preorder(self, t):
        if t:
            print(t.data, end=" ")
            self.preorder(t.lchild)
            self.preorder(t.rchild)
    def postorder(self, t):
        if t:
            self.postorder(t.lchild)
            self.postorder(t.rchild)
            print(t.data, end=" ")
    def count_nodes(self, t):
        if t is None:
            return 0
        return 1 + self.count_nodes(t.lchild) + self.count_nodes(t.rchild)
    def count_leaf_nodes(self, t):
        if t is None:
            return 0
        if t.lchild is None and t.rchild is None:
            return 1
        return self.count_leaf_nodes(t.lchild) + self.count_leaf_nodes(t.rchild)
    def find_min(self):
        t = self.root
        while t.lchild:
            t = t.lchild
        print("Minimum data = ", t.data)
    def find_max(self):
        t = self.root
        while t.rchild:
            t = t.rchild
        print("Maximum data = ", t.data)
    def find_height(self, t):
        if t == None:
            return 0
        lh = self.find_height(t.lchild)
        rh = self.find_height(t.rchild)
        if lh > rh:
            return lh + 1
        else:
            return rh + 1
    def search(self, t, data):
        if t is None:
            print("Data not found")
            return
        if t.data == data:
            print("Data found ")
            return
        elif data < t.data:
            return self.search(t.lchild, data)
        else:
            return self.search(t.rchild, data)
    def minValueNode(self, node):
        current = node
        while current.lchild is not None:
            current = current.lchild
        return current
    def deleteNode(self, root, key):
        if root is None:
            return root
        if key < root.data:
            root.lchild = self.deleteNode(root.lchild, key)
        elif key > root.data:
            root.rchild = self.deleteNode(root.rchild, key)
        else:
            if root.lchild is None:
                return root.rchild
            elif root.rchild is None:
                return root.lchild
            temp = self.minValueNode(root.rchild)
            root.data = temp.data
            root.rchild = self.deleteNode(root.rchild, temp.key)
        return root
    def operations(self):
        while True:
            print("\n1. Preorder\n2. Inorder\n3. Postorder\n4. count nodes \n5.count leaf nodes\n6.find minimum\n7.find maximum \n8.search data\n 9.find height\n10.delete node\n11.exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("Preorder sequence:")
                self.preorder(self.root)
            elif choice == 2:
                print("Inorder sequence:")
                self.inorder(self.root)
            elif choice == 3:
                print("Postorder sequence:")
                self.postorder(self.root)
            elif choice == 4:
                print("number of nodes = ", self.count_nodes(self.root))
            elif choice == 5:
                print("number of leaf nodes = ", self.count_leaf_nodes(self.root))
            elif choice == 6:
                self.find_min()
            elif choice == 7:
                self.find_max()
            elif choice == 8:
                data = int(input("Enter data to search"))
                self.search(self.root, data)
            elif choice == 9:
                print("height of the binary tree=", self.find_height(self.root))
            elif choice == 10:
                key = int(input("Enter data to delete"))
                self.deleteNode(self.root, key)
            elif choice == 11:
                break
            else:
                print("Invalid choice!")

bst = BST()
while True:
    data = int(input("Enter data (or -1 to stop): "))
    if data == -1:
        break
    bst.insert(data)
bst.operations()

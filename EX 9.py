class Node:
    def __init__(self, key, name):
        self.key = key
        self.name = name
        self.left = None
        self.right = None
        self.height = 1
class AVL:
    def height(self, n):
        return n.height if n else 0
    def balance(self, n):
        return self.height(n.left) - self.height(n.right) if n else 0
    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y
    def insert(self, root, key, name):
        if not root:
            return Node(key, name)
        if key < root.key:
            root.left = self.insert(root.left, key, name)
        elif key > root.key:
            root.right = self.insert(root.right, key, name)
        else:
            return root
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        b = self.balance(root)
        if b > 1 and key < root.left.key:
            return self.right_rotate(root)
        if b < -1 and key > root.right.key:
            return self.left_rotate(root)
        if b > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if b < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    def search(self, root, key):
        if not root or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)
    def min_node(self, root):
        while root.left:
            root = root.left
        return root
    def delete(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            temp = self.min_node(root.right)
            root.key = temp.key
            root.name = temp.name
            root.right = self.delete(root.right, temp.key)
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        b = self.balance(root)
        if b > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)
        if b > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if b < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)
        if b < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, "-", root.name)
            self.inorder(root.right)
    def preorder(self, root):
        if root:
            print(root.key, "-", root.name)
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, "-", root.name)
    def count(self, root):
        if not root:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)
avl = AVL()
root = None
while True:
    print("\n1.Insert\n2.Delete\n3.Search\n4.Inorder\n5.Preorder\n6.Postorder\n7.Count\n8.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        key = int(input("Enrollment ID: "))
        name = input("Student Name: ")
        root = avl.insert(root, key, name)
        print("Record inserted.")
    elif ch == 2:
        key = int(input("Enrollment ID: "))
        root = avl.delete(root, key)
        print("Record deleted.")
    elif ch == 3:
        key = int(input("Enrollment ID: "))
        r = avl.search(root, key)
        if r:
            print("Found:", r.key, "-", r.name)
        else:
            print("Record not found.")
    elif ch == 4:
        print("Inorder Traversal:")
        avl.inorder(root)
    elif ch == 5:
        print("Preorder Traversal:")
        avl.preorder(root)
    elif ch == 6:
        print("Postorder Traversal:")
        avl.postorder(root)
    elif ch == 7:
        print("Total Enrollments:", avl.count(root))
    elif ch == 8:
        break
    else:
        print("Invalid choice")

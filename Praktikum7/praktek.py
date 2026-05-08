# Nama: Ibra Arifa Istara
# NIM: J0403251029
# Kelas: A1

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res

    def postorderTraversal(self, root):
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data)
        return res

root = Node(29)
root.insert(9)
root.insert(49)
root.insert(49)
root.insert(19)
root.insert(39)
root.insert(59)
root.insert(14)

print("Nama    : Ibra Arifa Istara\nNIM     : J0403251029")
print(f"In-order Traversal    : {root.inorderTraversal(root)}")
print(f"Pre-order Traversal   : {root.preorderTraversal(root)}")
print(f"Post-order Traversal  : {root.postorderTraversal(root)}")

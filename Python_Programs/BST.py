class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinarySearchTree:

    def __init__(self):
        self.root = None

   
    def insert(self, key):
        newNode = Node(key)

        if self.root is None:
            self.root = newNode
            return

        current = self.root

        while True:
            if key <= current.key:
                if current.left is None:
                    current.left = newNode
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = newNode
                    return
                current = current.right

    def search(self, key):
        current = self.root

        while current is not None:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return False

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root is not None:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")

    def count(self, root):
        if root is None:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)

    def delete(self, root, key):

        if root is None:
          
        if key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
          
            if root.left is None and root.right is None:
                return None

            if root.left is None:
                return root.right

            if root.right is None:
                ret
            successor = root.right

            while successor.left is not None:
                successor = successor.left

            root.key = successor.key
            root.right = self.delete(root.right, successor.key)

        return root



bst = BinarySearchTree()


values = [27, 14, 35, 10, 19, 31, 42]

for value in values:
    bst.insert(value)

print("Inorder Traversal:")
bst.inorder(bst.root)

print("\nPreorder Traversal:")
bst.preorder(bst.root)

print("\nPostorder Traversal:")
bst.postorder(bst.root)

print("\nTotal number of nodes:", bst.count(bst.root))

key = 19

if bst.search(key):
    print("Search", key, ": Found")
else:
    print("Search", key, ": Not Found")


delete_key = 19
bst.root = bst.delete(bst.root, delete_key)

print("\nAfter deleting", delete_key, ":")
print("Inorder Traversal:")
bst.inorder(bst.root)

print("\nTotal number of nodes:", bst.count(bst.root))

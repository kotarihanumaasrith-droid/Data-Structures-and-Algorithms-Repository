class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def insert(self, root, val):
        if root is None:
            return Node(val)

        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)


if __name__ == "__main__":
    tree = BST()
    root = None
    root = tree.insert(root, 5)
    root = tree.insert(root, 3)
    root = tree.insert(root, 7)

    tree.inorder(root)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def print_tree(self, node):
        if node is None:
            return

        print(node.value)

        self.print_tree(node.left)
        self.print_tree(node.right)


tree = BinaryTree()

tree.root = Node(10)

tree.root.left = Node(5)
tree.root.right = Node(20)

tree.root.left.left = Node(2)
tree.root.left.right = Node(7)

tree.root.right.left = Node(15)
tree.root.right.right = Node(30)


tree.print_tree(tree.root)





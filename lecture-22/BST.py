class Node:

    def __init__(self, value):
        self.value = value
        self.count = 1
        self.height = 1
        self.left = None
        self.right = None

    @classmethod
    def get_height(cls, node):
        if node == None:
            return 0

        return node.height


class BinarySearchTree:

    def __init__(self):
        self.__root = None

    def insert(self, value):
        self.__root = self.__add_node_rec(self.__root, value)

    def __add_node_rec(self, node, value):
        if node == None:
            return Node(value)

        if value < node.value:
            node.left = self.__add_node_rec(node.left, value)
        elif value > node.value:
            node.right = self.__add_node_rec(node.right, value)
        else:
            node.count += 1

        node.height = max(Node.get_height(node.left), Node.get_height(node.right)) + 1

        return node


tree = BinarySearchTree()

items = [5, 9, 13, 7, 2, 10, 5, 7]

for item in items:
    tree.insert(item)

print(tree)

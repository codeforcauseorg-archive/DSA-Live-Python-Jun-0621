class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.__root = None

    def add_node(self, direction, value):
        self.__root = self.__add_node_rec(self.__root, direction, value)

    def __add_node_rec(self, node, direction, value, index=0):
        if index == len(direction):
            return Node(value)

        if direction[index] == "l":
            node.left = self.__add_node_rec(node.left, direction, value, index+1)
        elif direction[index] == "r":
            node.right = self.__add_node_rec(node.right, direction, value, index + 1)

        return node


file_ref = open("mytree.txt", "rt")
tree = BinaryTree()

for line in file_ref.readlines():
    items = line.split(" ")
    direction = items[:-1]
    value = int(items[-1])
    tree.add_node(direction, value)

print(tree)
class Node:

    def __init__(self, value):
        self.value = value
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

        node = BinarySearchTree.avl(node)
        return node

    @classmethod
    def left_rotate(cls, root):
        y = root
        x = y.right
        t2 = x.left

        x.left = y
        y.right = t2

        y.height = max(Node.get_height(y.left), Node.get_height(y.right)) + 1
        x.height = max(Node.get_height(x.left), Node.get_height(x.right)) + 1

        return x

    @classmethod
    def right_rotate(cls, root):
        x = root
        y = x.left
        t2 = y.right

        y.right = x
        x.left = t2

        x.height = max(Node.get_height(x.left), Node.get_height(x.right)) + 1
        y.height = max(Node.get_height(y.left), Node.get_height(y.right)) + 1

        return y

    @classmethod
    def avl(cls, node):

        if (Node.get_height(node.left) - Node.get_height(node.right)) > 1:
            if (Node.get_height(node.left.left) - Node.get_height(node.left.right)) <= -1:
                node.left = BinarySearchTree.left_rotate(node.left)
            node = BinarySearchTree.right_rotate(node)
        elif (Node.get_height(node.left) - Node.get_height(node.right)) < -1:
            if (Node.get_height(node.right.left) - Node.get_height(node.right.right)) >= 1:
                node.right = BinarySearchTree.right_rotate(node.right)
            node = BinarySearchTree.left_rotate(node)

        return node

    def height_tree(self):
        return Node.get_height(self.__root)


tree = BinarySearchTree()

# items = [5, 9, 13, 7, 2, 10, 5, 7]

for item in range(90000):
    tree.insert(item)

print(tree.height_tree())

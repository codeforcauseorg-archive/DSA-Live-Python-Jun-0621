class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class GeneralTable:

    def __init__(self):
        self.__data = []

    def set(self, key, value):
        for node in self.__data:
            if node.key == key:
                node.value = value
                return

        node = Node(key, value)
        self.__data.append(node)

    def get(self, key):
        for node in self.__data:
            if node.key == key:
                return node.value

        raise KeyError("{} is not in table".format(key))

    def contains(self, key):
        for node in self.__data:
            if node.key == key:
                return True

        return False


table = GeneralTable()
for i in range(1000000):
    if (i % 1000) == 0:
        print("reached", i)
    table.set(i, "value of {}".format(i))
# d = dict()
#
# d["hello"]


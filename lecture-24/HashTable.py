import time


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:

    def __init__(self):

        self.__data = []
        self.size = 0
        for i in range(10):
            self.__data.append([])

    def set(self, key, value):
        index = abs(hash(key)) % len(self.__data)
        bucket = self.__data[index]

        for node in bucket:
            if node.key == key:
                node.value = value
                return

        node = Node(key, value)
        self.size += 1
        bucket.append(node)

        if self.size // len(self.__data) > 5:
            self.rehash()

    def rehash(self):
        old = self.__data
        self.__data = []
        for i in range(2*len(old)):
            self.__data.append([])
        self.size = 0

        for bucket in old:
            for node in bucket:
                self.set(node.key, node.value)

    def get(self, key):
        index = abs(hash(key)) % len(self.__data)
        bucket = self.__data[index]

        for node in bucket:
            if node.key == key:
                return node.value

        raise KeyError("{} is not in table".format(key))

    def contains(self, key):
        index = abs(hash(key)) % len(self.__data)
        bucket = self.__data[index]

        for node in bucket:
            if node.key == key:
                return True

        return False

    def remove(self, key):
        index = abs(hash(key)) % len(self.__data)
        bucket = self.__data[index]

        for index, node in enumerate(bucket):
            if node.key == key:
                bucket.pop(index)
                self.size -= 1
                return

        raise KeyError("{} is not in table".format(key))


start = time.time()
table = HashTable()
for i in range(100000):
    table.set(i, "value of {}".format(i))
end = time.time()

print(end-start)
# d = dict()
#
# d["hello"]


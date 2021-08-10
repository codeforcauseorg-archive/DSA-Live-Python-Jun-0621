class Queue:

    def __init__(self):
        self.__data = []

    def insert(self, value):
        self.__data.append(None)
        for index in range(len(self.__data)-1, 0, -1):
            self.__data[index] = self.__data[index-1]
        self.__data[0] = value

    def delete(self):
        return self.__data.pop()

    def front(self):
        return self.__data[-1]

    def is_empty(self):
        return len(self.__data) == 0

    def __repr__(self):
        return "<--".join(map(str,self.__data))


q = Queue()

for i in range(100000):
    q.insert(i)


for i in range(100000):
    q.delete()


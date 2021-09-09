class Heap:

    def __init__(self, compare=None):
        self.__data = []
        if compare:
            self.compare = compare
        else:
            self.compare = lambda first, second: first - second

    def insert(self, value):
        self.__data.append(value)
        self.up_heap(len(self.__data) - 1)

    def up_heap(self, index):
        while index > 0:
            p_index = Heap.parent(index)
            if self.compare(self.__data[index], self.__data[p_index]) < 0:
                self.__data[index], self.__data[p_index] = self.__data[p_index], self.__data[index]
                index = p_index
            else:
                break

    def delete(self):
        value = self.__data[0]
        last = self.__data.pop()

        if len(self.__data) > 0:
            self.__data[0] = last
            self.downheap(0)

        return value

    def downheap(self, index):

        while True:
            min_index = index
            l_index = Heap.left(index)
            r_index = Heap.right(index)
            
            if (l_index < len(self.__data)) and self.compare(self.__data[l_index], self.__data[min_index]) < 0:
                min_index = l_index

            if (r_index < len(self.__data)) and self.compare(self.__data[r_index], self.__data[min_index]) < 0:
                min_index = r_index

            if min_index == index:
                break
            else:
                self.__data[min_index], self.__data[index] = self.__data[index], self.__data[min_index]
                index = min_index

    def size(self):
        return len(self.__data)

    @classmethod
    def parent(cls, index):
        return (index-1)//2

    @classmethod
    def left(cls, index):
        return 2 * index + 1

    @classmethod
    def right(cls, index):
        return 2 * index + 2


heap = Heap(compare=lambda first, second: second - first)

li = 10, 20, 31, 12, 54, 13, 5, 24, 675, 23


for item in li:
    heap.insert(item)

for i in range(len(li)):
    print(heap.delete())
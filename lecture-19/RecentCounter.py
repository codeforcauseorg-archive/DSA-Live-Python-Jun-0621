# https://leetcode.com/problems/number-of-recent-calls

class RecentCounter:

    def __init__(self):
        self.__data = [None] * 10
        self.__front = 0
        self.__end = -1
        self.__size = 0

    def insert(self, value):

        if not self.is_full():
            self.__end = (self.__end + 1) % len(self.__data)
            self.__data[self.__end] = value
            self.__size += 1
        else:
            space = [None] * (2 * len(self.__data))
            for index in range(self.__size):
                space[index] = self.__data[(index + self.__front) % len(self.__data)]
            self.__front = 0
            self.__end = self.__size - 1
            self.__data = space
            self.insert(value)

    def delete(self):
        value = self.__data[self.__front]
        self.__front = (self.__front + 1) % len(self.__data)
        self.__size -= 1
        return value

    def front(self):
        return self.__data[self.__front]

    def is_empty(self):
        return self.__size == 0

    def is_full(self):
        return self.__size == len(self.__data)

    def ping(self, t: int) -> int:

        self.insert(t)

        while (self.front() < (t - 3000)):
            self.delete()

        return self.__size

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


class LinkedList:

    def __init__(self):
        self.__head = None

    def get(self, index):
        node = self.__get_by_index(index)
        return node.value

    def insert_first(self, value):
        node = Node(value)
        node.next = self.__head
        self.__head = node

    def insert_last(self, value):
        if not self.__head:
            self.insert_first(value)
            return

        last = self.__head
        while last.next:
            last = last.next

        node = Node(value)
        last.next = node

    def __get_by_index(self, index):
        current = self.__head
        for i in range(0, index):
            current = current.next
        return current

    def insert(self, value, index):
        if index == 0:
            self.insert_first(value)
            return

        node = Node(value)

        prev = self.__get_by_index(index-1)
        node.next = prev.next
        prev.next = node

    def remove_first(self):
        value = self.__head.value
        self.__head = self.__head.next
        return value

    def remove_last(self):
        if not self.__head.next:
            return self.remove_first()

        slast = self.__head
        while slast.next.next:
            slast = slast.next

        last = slast.next
        slast.next = None

        return last.value

    def remove(self, index):
        if index == 0:
            return self.remove_first()

        prev = self.__get_by_index(index-1)
        value = prev.next.value
        prev.next = prev.next.next
        return value

    def is_empty(self):
        return not self.__head

    def __repr__(self):
        output = []
        temp = self.__head
        while temp:
            output.append(temp.value)
            temp = temp.next

        return " => ".join(output)


class Stack:

    def __init__(self):
        self.__data = LinkedList()

    def push(self, value):
        self.__data.insert_first(value)

    def pop(self):
        return self.__data.remove_first()

    def top(self):
        return self.__data.get(0)

    def is_empty(self):
        return self.__data.is_empty()


ll = LinkedList()
ll.insert_last("ravi")
ll.insert_last("laila")
ll.insert_first("neha")

ll.insert("sumit", 1)
ll.insert("teena", 4)
ll.insert("monu", 0)

print(ll.remove_first())
print(ll.remove_last())
print(ll.remove(1))

print(ll)

# ravi = Node("ravi")
#
# print(not ravi)




class Stack:

    def __init__(self):
        self.__data = []

    def push(self, value):
        self.__data.append(value)

    def pop(self):
        return self.__data.pop()

    def top(self):
        return self.__data[-1]

    def is_empty(self):
        return len(self.__data) == 0

    def __repr__(self):
        return "<--".join(map(str,self.__data))


st = Stack()
st.push(10)
print(st)
st.push(20)
print(st)
st.push(50)
print(st)
st.push(12)
print(st)

print(st.pop())
print(st)
print(st.pop())
print(st)
print(st.pop())
print(st)
print(st.pop())
print(st)







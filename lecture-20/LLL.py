class Node:

    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


ravi = Node('ravi')
laila = Node('laila')
varun = Node('varun')
ritu = Node('ritu')
yash = Node('yash')
munni = Node('munni')

ravi.next = laila
laila.next = varun
varun.next = ritu
ritu.next = yash
yash.next = munni

head = ravi

print(head.next.next.next.value)



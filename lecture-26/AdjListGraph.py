class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbours = []

class AdjListGraph:

    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, value):
        if value not in self.vertices:
            self.vertices[value] = Vertex(value)

    def add_edge(self, first, second):
        if (first in self.vertices) and (second in self.vertices):
            vfirst = self.vertices[first]
            vsecond = self.vertices[second]
            vfirst.neighbours.append(vsecond)
            vsecond.neighbours.append(vfirst)

    def DFT(self, source):

        stack = []
        visited = set()

        svertex = self.vertices[source]

        stack.append(svertex)
        visited.add(svertex)

        while len(stack) > 0:

            top = stack.pop()
            print(top.value)

            for padosi in top.neighbours:
                if padosi not in visited:
                    visited.add(padosi)
                    stack.append(padosi)

    def DFS(self, source, target):

        stack = []
        visited = set()

        svertex = self.vertices[source]

        stack.append(svertex)
        visited.add(svertex)

        while len(stack) > 0:

            top = stack.pop()

            if top.value == target:
                return True

            for padosi in top.neighbours:
                if padosi not in visited:
                    visited.add(padosi)
                    stack.append(padosi)

        return False

    def BFT(self, source):

        queue = []
        visited = set()

        svertex = self.vertices[source]

        queue.append(svertex)
        visited.add(svertex)

        while len(queue) > 0:

            front = queue.pop(0)
            print(front.value)

            for padosi in front.neighbours:
                if padosi not in visited:
                    visited.add(padosi)
                    queue.append(padosi)





    def represent(self):
        for vertex in self.vertices.values():
            print(vertex.value, end="-> ")
            for neighbour in vertex.neighbours:
                print(neighbour.value, end=", ")

            print()


graph = AdjListGraph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

graph.add_edge("A", "B")
graph.add_edge("B", "D")
graph.add_edge("A", "C")
graph.add_edge("A", "D")


graph.represent()


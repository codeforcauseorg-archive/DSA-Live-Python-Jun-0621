class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbours = {}

class AdjListGraph:

    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, value):
        if value not in self.vertices:
            self.vertices[value] = Vertex(value)

    def add_edge(self, first, second, weight):
        if (first in self.vertices) and (second in self.vertices):
            vfirst = self.vertices[first]
            vsecond = self.vertices[second]
            vfirst.neighbours[vsecond] = weight
            vsecond.neighbours[vfirst] = weight

    def min_spanning_tree(self):

        edges = []

        for vertex in self.vertices.values():
            # print(vertex.neighbours.items())
            for neighbour, weight in vertex.neighbours.items():
                edges.append([weight, vertex.value, neighbour.value])

        sorted_edges = sorted(edges)

        acc = 0

        for [weight, source, dest] in sorted_edges:
            if self.union(source, dest):
                acc += weight

        return acc




        # parents = {}
        # for vertex in self.vertices:
        #     parents[vertex.value] = None



    def union(self, parents, first, second):
        first = self.find(parents, first)
        second = self.find(parents, second)

        if first == second:
            return False
        else:
            parents[first] = second

    def find(self, parents, item):
        while parents[item] != None:
            item = parents[item]
        return item


    def represent(self):
        for vertex in self.vertices.values():
            print(vertex.value, end="-> ")
            for neighbour in vertex.neighbours:
                print("[{} : {}]".format(neighbour.value, vertex.neighbours[neighbour]), end=", ")

            print()




graph = AdjListGraph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

graph.add_edge("A", "B", 10)
graph.add_edge("B", "C", 15)
graph.add_edge("D", "C", 10)
graph.add_edge("A", "D", 20)

graph.min_spanning_tree()


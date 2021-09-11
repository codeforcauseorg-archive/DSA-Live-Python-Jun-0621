class Solution:
    def findRedundantConnection(self, edges):

        n = len(edges)

        parents = {}

        for i in range(1, n + 1):
            parents[i] = None

        for (source, dest) in edges:
            if not self.union(parents, source, dest):
                return [source, dest]

    def union(self, parents, first, second):
        first = self.find(parents, first)
        second = self.find(parents, second)

        if first == second:
            return False
        else:
            parents[first] = second

        return True

    def find(self, parents, item):
        while parents[item] != None:
            item = parents[item]
        return item
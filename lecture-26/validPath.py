class Solution:
    def validPath(self, n, edges, start, end):

        parents = dict()

        for i in range(n):
            parents[i] = None

        for edge in edges:
            self.union(parents, edge[0], edge[1])

        print(parents)

        print(self.find(parents, start), self.find(parents, end))

        return self.find(parents, start) == self.find(parents, end)

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


sol = Solution()

edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]

sol.validPath(10, edges, 5, 9)
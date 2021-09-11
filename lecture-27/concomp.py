class Solution:
    def maxAreaOfIsland(self, grid):

        components = []

        stack = []
        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 0:
                    continue

                if (i, j) in visited:
                    continue

                component = []

                stack.append((i, j))
                visited.add((i, j))

                while len(stack) > 0:

                    (i, j) = stack.pop()

                    component.append((i, j))

                    for padosi in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if (padosi[0] in range(rows)) and (padosi[1] in range(cols)) and (padosi not in visited) and (grid[padosi[0]][padosi[1]] == 1):
                            visited.add(padosi)
                            stack.append(padosi)

                components.append(component)

        sols = list[map(lambda comp: len(comp), components)]

        return max(sols)


sol = Solution()

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(sol.maxAreaOfIsland(grid))
# https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        output = []
        count = 0
        index = 0
        value = 0

        while (count <= n) and len(target) > index:

            current = target[index]

            for item in range(value + 1, current):
                output.append("Push")
                output.append("Pop")

            output.append("Push")
            index += 1
            count += 1
            value = current

        return output





# https://leetcode.com/problems/binary-watch/

class Solution:
    def readBinaryWatch(self, turnedOn):
        self.solutions = []
        watch = [False] * 10
        self.watchRec(turnedOn, watch)
        return self.solutions

    def watchRec(self, n, watch, index=0, h=0, m=0):

        if (h > 11) or (m > 59):
            return

        if n == 0:
            self.solutions.append("{}:{}".format(h, str(m).zfill(2)))
            return

        if index == len(watch):
            return

        if index < 4:
            h_gen = 2 ** index
            watch[index] = True
            self.watchRec(n - 1, watch, index + 1, h + h_gen, m)
            watch[index] = False

            self.watchRec(n, watch, index + 1, h, m)
        else:
            m_gen = 2 ** (index - 4)
            watch[index] = True
            self.watchRec(n - 1, watch, index + 1, h, m + m_gen)
            watch[index] = False

            self.watchRec(n, watch, index + 1, h, m)


sol = Solution()
sols = sol.readBinaryWatch(2)
print(sols)
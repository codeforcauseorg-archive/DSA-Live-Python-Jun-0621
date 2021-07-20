class Solution:

    def to_letters(self, digit):
        letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        return list(letters[digit])

    def letterCombinations(self, digits):
        self.solution = []
        if digits:
            self.letterCombinationsrec(digits, "", 0)
        return self.solution

    def letterCombinationsrec(self, digits, proc, index):
        if index == len(digits):
            self.solution.append(proc)
            return

        digit = int(digits[index])

        letters = self.to_letters(digit)

        for letter in letters:
            self.letterCombinationsrec(digits, proc + letter, index + 1)



problem = Solution()

print(problem.letterCombinations("23"))
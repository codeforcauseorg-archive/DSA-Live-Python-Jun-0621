# https://leetcode.com/problems/remove-outermost-parentheses

class Solution:
    def removeOuterParentheses(self, s):

        output = []
        count = 0

        for letter in s:

            if letter == "(":
                if count != 0:
                    output.append(letter)
                count += 1
            else:
                if count != 1:
                    output.append(letter)
                count -= 1

        return "".join(output)
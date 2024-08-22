class Solution:
    def balancedStringSplit(self, s: str) -> int:

        R = 0
        L = 0
        output = 0

        for i in s:
            if i == "R":
                R += 1
            if i == "L":
                L += 1
            if R == L:
                output += 1

        return output

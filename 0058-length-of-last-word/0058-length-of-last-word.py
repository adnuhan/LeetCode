class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = 0
        hold = 0
        for i in s:
            if i != " ":
                last += 1
                hold = last
            else:
                last = 0
        return hold
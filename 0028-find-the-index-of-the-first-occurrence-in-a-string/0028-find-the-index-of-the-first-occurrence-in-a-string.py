class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        end = len(needle)
        while end <= len(haystack):
            if haystack[start: end] == needle:
                return start
            else:
                start += 1
                end += 1
        return -1
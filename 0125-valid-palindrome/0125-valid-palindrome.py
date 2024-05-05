class Solution:
    def isPalindrome(self, s: str) -> bool:
        index = -1
        first = ""
        last = ""
        for i in s:
            if i.isalpha() or i.isnumeric():
                first += i.lower()
            if s[index].isalpha() or s[index].isnumeric():
                last += s[index].lower()
            index -= 1
        if first == last:
            return True
        return False

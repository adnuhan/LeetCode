class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        last = len(s) - 1
        add = ""
        for i in range(last):
            add = s[last]
            s.insert(i, add)
            s.pop()
        
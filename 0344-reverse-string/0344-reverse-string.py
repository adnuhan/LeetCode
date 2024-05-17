class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        last_index = len(s) - 1
        word = ""
        for i in range(last_index):
            word = s[last_index]
            s.insert(i, word)
            s.pop()
        
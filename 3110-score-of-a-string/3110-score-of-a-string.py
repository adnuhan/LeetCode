class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = 0
        
        for i in range(len(s) - 1):
            output += abs(ord(s[i]) - ord(s[i + 1]))
        return output
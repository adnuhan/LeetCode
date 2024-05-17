class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        length = {}
        output = len(t) - 1        
        if len(s) != len(t):
            return False
        for i in s:
            if i not in length:
                length[i] = 0
            length[i] += 1
        
        for j in t:
            if j not in length:
                return False
            elif length[j] > 0:
                length[j] -= 1
            else:
                return False
        return True
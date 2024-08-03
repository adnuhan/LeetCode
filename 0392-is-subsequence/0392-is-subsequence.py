class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) <= 1:
            return True if s in t else False
        
        if len(s) > len(t):
            return False

        i = 0
        
        for j in t:
            if i < len(s) and s[i] == j:
                i += 1
                
        return i == len(s)

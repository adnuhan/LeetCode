class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        t_list = list(t)
        
        for i in range(len(s)):
            if s[i] in t_list:
                t_list.remove(s[i])

        return "".join(t_list)

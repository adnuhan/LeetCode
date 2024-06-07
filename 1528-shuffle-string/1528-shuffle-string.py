class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        s_list = list(s)
        
        for i in range(len(s)):
            s_list[indices[i]] = s[i]
        
        return "".join(s_list)

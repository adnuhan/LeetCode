class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s_list = s.split(" ", (len(s)))
        output = ""

        for i in range(k):
            if 0 < i < k:
                output += " "
            output += s_list[i]
        
        return output
            
        
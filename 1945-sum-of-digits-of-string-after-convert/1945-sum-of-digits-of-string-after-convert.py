class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        s_integer = ""
        temp = 0
        output = 0

        for i in s:
            s_integer += (str(ord(i) - 96))

        while k > 0:
            for i in s_integer:
                temp += int(i)
            s_integer = str(temp)
            output = temp
            temp = 0
            k -= 1
        
        return output
        
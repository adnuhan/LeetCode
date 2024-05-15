class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1) - 1
        j = len(num2) - 1
        
        carry = 0
        result = []
        
        while i >= 0 or j >= 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            
            xy = carry + x + y
            
            result.append(str(xy % 10))
            
            carry = xy // 10
            
            i -= 1
            j -= 1
            
        if carry:
            result.append(str(carry))
            
        return "".join(reversed(result))
            
        
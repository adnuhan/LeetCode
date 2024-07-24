class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        
        last = len(num) - 1
        output = ""
        
        for i in num:
            if num[last] == "0":
                last -= 1
                
        for j in range(last + 1):
            output += num[j]
        
        return output
        
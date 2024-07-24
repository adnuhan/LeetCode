class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        
        j = len(num) - 1
        
        for i in num:
            if num[j] != "0":
                break
            j -= 1
            
        return num[:j + 1]
        
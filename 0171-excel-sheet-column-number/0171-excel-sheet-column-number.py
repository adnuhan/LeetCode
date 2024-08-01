class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        output = 0
        index = len(columnTitle) - 1
        
        for i in range(len(columnTitle)):
            output += (ord(columnTitle[index]) - 64) * 26 ** i
            index -= 1
        
        return output
        
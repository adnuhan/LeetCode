class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        
        output = 0
        
        for char in range(len(s)):
            output += abs(char - (t.index(s[char])))
            
        return output

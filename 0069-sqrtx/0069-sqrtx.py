class Solution:
    def mySqrt(self, x: int) -> int:
        output = 0
        odd = 1
        rem = x
        
        while rem >= odd:
            rem = rem - odd
            odd += 2
            output += 1
    
        return output

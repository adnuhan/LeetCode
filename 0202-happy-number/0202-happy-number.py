class Solution:
    def isHappy(self, n: int) -> bool:

        count = 7
        happy = 0
        
        while count > 0:
    
            while n != 0:
                happy += (n % 10) ** 2
                n = n // 10
                
            if happy != 1:
                n = happy
                happy = 0
                count -= 1
            
            else:
                return happy

        return happy
    
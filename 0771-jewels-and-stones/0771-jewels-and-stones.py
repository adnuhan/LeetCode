class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        output = 0
        
        for stone in jewels:
            output += stones.count(stone)
            
        return output

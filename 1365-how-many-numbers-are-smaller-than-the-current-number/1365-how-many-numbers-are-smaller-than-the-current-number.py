class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        output = []
        small = 0
        
        for i in nums:
            small = 0
            for j in nums:
                if j < i:
                    small += 1
            output.append(small)
                
        return output
    
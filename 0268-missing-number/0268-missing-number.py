class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        output = 0
        
        for i in range(len(nums) + 1):
            output += i
            
        return output - sum(nums)
    
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        output = 0
        n = len(nums)
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    output += 1
                    
        return output
        
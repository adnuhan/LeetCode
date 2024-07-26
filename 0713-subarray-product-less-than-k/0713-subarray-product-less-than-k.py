class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        output = 0
        product = 1
        i = 0
        
        for j in range(len(nums)):
            product *= nums[j]
            
            while i <= j and product >= k:
                product = product // nums[i]
                i += 1
            output += (j - i + 1)
        
        return output
    
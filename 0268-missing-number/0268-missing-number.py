class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        l = 0
        r = len(nums)
        
        while l <= r:
            if l not in nums:
                return l
            if r not in nums:
                return r
            l += 1
            r -= 1

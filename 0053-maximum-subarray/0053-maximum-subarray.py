class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        mx = -10000
        curr_sum = 0
        
        for i in nums:
            curr_sum += i
            if curr_sum > mx:
                mx = curr_sum
            if curr_sum < 0:
                curr_sum = 0

        return mx

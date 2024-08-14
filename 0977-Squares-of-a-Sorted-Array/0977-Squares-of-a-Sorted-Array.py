class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        for n in range(len(nums)):
            nums[n] = nums[n] * nums[n]

        return sorted(nums)

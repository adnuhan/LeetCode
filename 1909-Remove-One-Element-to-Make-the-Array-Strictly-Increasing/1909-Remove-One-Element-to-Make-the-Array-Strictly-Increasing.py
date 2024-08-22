class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:

        situation = False
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                if situation:
                    return False
                if i > 1 and nums[i] <= nums[i-2]:
                    nums[i] = nums[i-1]

                situation = True
        
        return True

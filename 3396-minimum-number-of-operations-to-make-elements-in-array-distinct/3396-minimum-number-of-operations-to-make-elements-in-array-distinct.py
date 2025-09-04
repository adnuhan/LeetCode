class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        seen = set()
        i = len(nums) - 1

        while i >= 0 and nums[i] not in seen:
            seen.add(nums[i])
            i -= 1
    
        return ceil((i + 1) / 3)

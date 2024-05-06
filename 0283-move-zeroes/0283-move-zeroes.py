class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_index = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                swap = nums[last_index]
                nums[last_index], nums[i] = nums[i], swap
                last_index += 1

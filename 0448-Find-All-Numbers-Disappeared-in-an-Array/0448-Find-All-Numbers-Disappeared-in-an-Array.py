class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        output = [num for num in range(1, len(nums) + 1)]

        return set(output) - set(nums)

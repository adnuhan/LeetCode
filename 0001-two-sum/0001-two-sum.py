class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for index, value in enumerate(nums):
            seen_num = target - value
            if seen_num in seen:
                return([seen[seen_num], index])
            seen[value] = index
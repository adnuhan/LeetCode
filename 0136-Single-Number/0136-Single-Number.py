class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        output = 0

        for num in nums:
          output ^= num

        return output

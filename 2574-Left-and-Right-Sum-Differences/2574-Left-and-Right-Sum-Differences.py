class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        total = sum(nums)
        prefix_sum = 0
        answer = []

        for i in range(len(nums)):
            if i == 0:
                prefix_sum += nums[i]
                answer.append(abs((prefix_sum - nums[i]) - (total - prefix_sum)))
            elif i == len(nums) - 1:
                prefix_sum += nums[i]
                answer.append(abs((prefix_sum - nums[i]) - (total - prefix_sum)))
            elif i != 0 and i != len(nums) - 1:
                prefix_sum += nums[i]
                answer.append(abs((prefix_sum - nums[i]) - (total - prefix_sum)))

        return answer

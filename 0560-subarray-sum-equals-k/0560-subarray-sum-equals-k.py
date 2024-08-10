class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = {0: 1}
        cur_sum = 0
        output = 0

        for n in nums:
            cur_sum += n
            diff = cur_sum - k
            output += prefix_sum.get(diff, 0)
            prefix_sum[cur_sum] = 1 + prefix_sum.get(cur_sum, 0)

        return output

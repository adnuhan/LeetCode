class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        output = []
        add = 0

        for i in range(len(nums)):
            output.append(nums[i])
            add = nums[i]
            for j in nums[i+1:]:
                add += j
                output.append(add)
                
            add = 0
        output.sort()

        return sum(output[(left - 1):right]) % 1000000007

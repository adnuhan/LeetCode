class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        output = 0

        for x in range(len(nums)):
            if nums[x] == 1 or (nums[x] - 1) % 3 == 0:
                nums[x] -= 1
                output += 1
            elif (nums[x] + 1) % 3 == 0:
                nums[x] += 1
                output += 1
                
        return output

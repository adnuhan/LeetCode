class Solution:
    def minimumAverage(self, nums: List[int]) -> float:

        average = []

        while len(nums) > 0:
            average.append((min(nums) + max(nums)) / 2)
            nums.remove(min(nums))
            nums.remove(max(nums))
        
        average.sort()

        return average[0]
        

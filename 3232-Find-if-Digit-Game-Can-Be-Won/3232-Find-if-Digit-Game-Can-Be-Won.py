class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:

        single = 0
        double = 0

        for num in nums:
            if num < 10:
                single += num
            elif num > 9:
                double += num

        return single != double
        

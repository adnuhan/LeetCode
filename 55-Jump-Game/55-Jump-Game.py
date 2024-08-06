class Solution:
    def canJump(self, nums: List[int]) -> bool:

        index = 0

        for i in nums:
            if index < 0:
                return False
            elif i > index:
                index = i
            index -= 1
 
        return True

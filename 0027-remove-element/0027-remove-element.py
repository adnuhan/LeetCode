class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in nums:
            love = nums
            if i != val:
                nums[k] = i
                k += 1
        return k

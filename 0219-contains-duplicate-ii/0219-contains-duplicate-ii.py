class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hasmap = {}

        for i,j in enumerate(nums):
            if j in hasmap and abs(i - hasmap[j]) <= k:
                return True
            hasmap [j] = i
        
        return False

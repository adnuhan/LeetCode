class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
    
        hash_map = {}

        for i in set(nums):
            hash_map[i] = nums.count(i)

        return sorted(nums, key=lambda x: (hash_map[x], -x))

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        output = 0
        hash_map = {}

        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        
        
        for value in hash_map.values():
            if value > 0:
                output += int(value * (value - 1) / 2)
        
        
        return output

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        output = 0
        
        for num in nums:
            if num + diff in nums and num + diff * 2 in nums:
                output += 1
        
        return output

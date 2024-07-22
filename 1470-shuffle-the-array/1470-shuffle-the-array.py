class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        output = []
        i = 0
        j = n
        
        while j <= len(nums) - 1:
            output.append(nums[i])
            output.append(nums[j])
            i += 1
            j += 1

        return output
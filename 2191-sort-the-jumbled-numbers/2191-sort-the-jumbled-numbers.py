class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        mapped = []
        output = []
        shuffled = ""

        for x in nums:
            num = str(x)
            for y in range(len(num)):
                shuffled += str(mapping[int(num[y])])
            mapped.append(shuffled)
            shuffled = ""
        
        for z in sorted(range(len(mapped)), key=lambda k: int(mapped[k])):
            output.append(nums[z])
        
        return output

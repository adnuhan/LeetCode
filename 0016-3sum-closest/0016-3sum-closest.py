class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        output = sum(nums[:3])
        
        for x in range(len(nums) - 2):
            y = x + 1
            z = len(nums) - 1
            
            while y < z:
                addition = nums[x] + nums[y] + nums[z]
                
                if abs(addition - target) < abs(output - target):
                    output = addition
                if addition < target:
                    y += 1
                else:
                    z -= 1
                    
        return output
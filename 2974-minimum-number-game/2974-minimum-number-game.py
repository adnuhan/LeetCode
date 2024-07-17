class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        
        alice = 0
        bob = 0
        output = []
        
        while nums:
            alice = min(nums)
            nums.remove(alice)
            bob = min(nums)
            nums.remove(bob)
            output.append(bob)
            output.append(alice)
            
        return output

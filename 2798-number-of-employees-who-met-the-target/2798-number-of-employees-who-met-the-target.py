class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        
        output = 0
        
        for num in hours:
            if num >= target:
                output += 1

        return output

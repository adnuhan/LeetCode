class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        
        i = 0
        j = len(hours) - 1
        output = 0
        
        while i <= j:
            if i == j:
                if hours[i] >= target:
                    output += 1
            else:
                if hours[i] >= target:
                    output += 1
                if hours[j] >= target:
                    output += 1
            i += 1
            j -= 1
        
        return output
        
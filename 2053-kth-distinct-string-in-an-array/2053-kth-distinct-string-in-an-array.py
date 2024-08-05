class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        output = []
        
        for i in arr:
            if arr.count(i) == 1 and i not in output:
                output.append(i)
        
        if len(output) >= k:
            return output[k - 1]
            
        else:
            return ""

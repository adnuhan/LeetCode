class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
   
        output = [num for sublist in matrix for num in sublist]
        output.sort()
        
        return output[k - 1]

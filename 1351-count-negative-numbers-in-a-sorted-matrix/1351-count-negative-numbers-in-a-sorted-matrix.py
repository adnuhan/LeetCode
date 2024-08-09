class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        output = 0

        for i in grid:
            output += len(list(filter(lambda x: (x < 0), i)))
        
        return output
        

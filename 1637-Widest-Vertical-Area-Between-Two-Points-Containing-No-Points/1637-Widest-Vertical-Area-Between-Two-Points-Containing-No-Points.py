class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        points.sort()
        output = 0
        
        for i in range(1,len(points)):
            curr = points[i][0] - points[i-1][0]
            output = max(curr, output)
        
        return output

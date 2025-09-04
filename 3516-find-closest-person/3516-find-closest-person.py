class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:

        p1 = abs(x - z)
        p2 = abs(y - z)
        
        if p1 < p2:
            return 1
        if p2 < p1:
            return 2
        return 0

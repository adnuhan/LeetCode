class Solution:
    def climbStairs(self, n: int) -> int:
        
        staircase = [0, 1, 2, 3]

        for i in range(4, n+1):
            staircase.append(staircase[i - 1] + staircase[i - 2])

        return staircase[n]
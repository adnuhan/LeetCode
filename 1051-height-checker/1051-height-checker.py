class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        expected = sorted(heights)
        output = 0

        for x in range(len(heights)):
            if heights[x] != expected[x]:
                output += 1

        return output

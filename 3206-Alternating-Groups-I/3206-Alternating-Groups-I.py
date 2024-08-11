class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:

        output = 0

        for i in range(-1, len(colors) - 1):
            if colors[i - 1] != colors[i] and colors[i] != colors[i + 1]:
                output += 1

        return output

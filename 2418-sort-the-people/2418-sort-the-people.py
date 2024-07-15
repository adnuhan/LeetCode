class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        output = []
        
        for height in range(len(heights)):
            max_height = max(heights)
            index = heights.index(max_height)
            heights[index] = 0
            output.append(names[index])

        return output

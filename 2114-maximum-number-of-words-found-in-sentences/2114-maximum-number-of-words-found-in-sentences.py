class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
    
        output = 0

        for sentence in sentences:
            maximum = sentence.count(" ") + 1
            if maximum > output:
                output = maximum

        return output

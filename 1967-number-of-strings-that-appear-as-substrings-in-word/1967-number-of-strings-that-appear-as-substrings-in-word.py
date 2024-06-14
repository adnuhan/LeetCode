class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        
        output = 0

        for letter in patterns:
            if letter in word:
                output += 1

        return output

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        output = 0

        for word in words:
            for letter in word:
                if letter in allowed:
                    pass
                else:
                    output -= 1
                    break
            output += 1

        return output

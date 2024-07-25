class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        output = 0

        for word in words:
            if word[:len(pref)] == pref:
                output += 1
    
        return output

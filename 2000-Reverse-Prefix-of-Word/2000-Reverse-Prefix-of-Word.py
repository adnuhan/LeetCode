class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        reverse = word[0: word.find(ch) + 1]

        return word.replace(reverse, reverse[::-1])
        

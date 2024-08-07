class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        text = list(text.split(" "))
        output = len(text)

        for word in text:
            for char in brokenLetters:
                if char in word:
                    output -= 1
                    break
  
        return output

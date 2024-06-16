class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        character = 0
        output = ""

        while character <= len(s) - 1:
            if "#" in s[character: character + 3]:
                output += (chr(int(s[character:(character + 2)]) + 96))
                character += 3
            else:
                output += chr(int(s[character]) + 96)
                character += 1

        return output
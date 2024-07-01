class Solution:
    def reverseWords(self, s: str) -> str:

        current_word = ""
        output = ""

        for sentence in range(len(s)):
            if s[sentence] != " " and sentence <= len(s):
                current_word += s[sentence]
            else:
                output += current_word[::-1]
                output += " "
                current_word = ""

        output += current_word[::-1]
        
        return output

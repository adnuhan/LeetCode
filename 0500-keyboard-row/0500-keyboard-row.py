class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        index = 0
        index_1 = 0
        is_in = ""
        output = []

        for word in words:

            while index < (len(word)) and index_1 < 3:
                check = keyboard[index_1]
                if word[index].lower() not in check and index_1 <= len(keyboard):
                    index_1 += 1
                    index = 0
                    is_in = ""
                else:
                    is_in += word[index]
                    index += 1

            if is_in == word:
                output.append(word)
                is_in = ""

            index_1 = 0
            index = 0
        
        return output

class Solution:
    def sortSentence(self, s: str) -> str:
        
        s_list = s.split()
        output = [None] * len(s_list)
        
        for word in s_list:
            current_word = word[0: (len(word) - 1)]
            current_word_number = int(word[-1]) - 1
            output.pop(current_word_number)
            output.insert(current_word_number, current_word)
        
        return " ".join(output)
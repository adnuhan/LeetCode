class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        word_list = list(word)
        output_list = []
        index = 0

        while index <= (len(word_list) - 1):
            if word_list[index].islower() and word_list[index].upper() in word_list:
                if word_list[index].upper() not in output_list:
                    output_list.append(word_list[index].upper())

            index += 1

        return len(output_list)
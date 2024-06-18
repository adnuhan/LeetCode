class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        
        
        output = 0
        reverse = ""
        index = 1

        while len(words) > 1:
            reverse = words[0]
            for i in range(1, len(words)):
                if reverse[::-1] == words[i]:
                    output += 1
                    words.remove(words[i])
                    words.remove(words[0])
                    break
                elif i == len(words) - 1:
                    words.remove(words[0])
                    break

        return output

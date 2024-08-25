class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        hashmap = {}
        output = ""
        n = 97

        for i in key:
            if i not in hashmap and i != ' ':
                hashmap[i] = chr(n)
                n += 1

        for j in message:
            if j == ' ':
                output += ' '
            else:
                output += hashmap[j]

        return output

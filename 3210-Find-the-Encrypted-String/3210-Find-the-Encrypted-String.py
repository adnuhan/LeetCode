class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        
        output = []

        if k > len(s):
            k = k % len(s)

        for n in range(len(s)):
            index = n + k
            if index < len(s):
                output.append(s[index])
            else:
                index -= len(s)
                output.append(s[index])

        return "".join(output)
    

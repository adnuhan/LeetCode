class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        output = []
        while columnNumber > 0:
            columnNumber -= 1
            quotient, rem = divmod(columnNumber, 26)
            output.append(chr(ord('A') + rem))
            columnNumber = quotient
        return ''.join(output[::-1])

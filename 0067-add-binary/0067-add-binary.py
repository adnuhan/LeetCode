class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_num = 0
        b_num = 0
        a_power = len(a) - 1
        b_power = len(b) - 1
        output = ""

        for i in range(len(a)):
            a_num += int(a[i]) * 2 ** a_power
            a_power -= 1
        for i in range(len(b)):
            b_num += int(b[i]) * 2 ** b_power
            b_power -= 1
        sum = a_num + b_num
        while sum > 0:
            rem = sum % 2
            output = str(rem) + output
            sum = sum // 2
        if output == "":
            return "0"
        return output
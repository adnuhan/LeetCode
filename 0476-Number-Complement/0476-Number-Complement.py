class Solution:
    def findComplement(self, num: int) -> int:

        complement_str = ""

        for i in bin(num)[2:]:
            if i == "1":
                complement_str += "0"
            else:
                complement_str += "1"

        return int(complement_str, 2)

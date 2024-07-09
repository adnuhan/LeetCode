class Solution:
    def defangIPaddr(self, address: str) -> str:

        output = ""

        for i in address:
            if i == ".":
                output += "[.]"
            else:
                output += i
        
        return output

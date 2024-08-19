class Solution:
    def countBits(self, n: int) -> List[int]:

        output = [0]
    
        for i in range(1, n + 1):
            output.append(bin(i).count("1"))

        return output

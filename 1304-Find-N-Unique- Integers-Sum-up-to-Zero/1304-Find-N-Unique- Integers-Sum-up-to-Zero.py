class Solution:
    def sumZero(self, n: int) -> List[int]:

        if n == 1:
            return [0]

        output = []

        if n % 2 != 0:
            k = 1
            n = (n // 2) + 1
            output.append(0)
            
        else:
            k = n // 2

        for i in range(k, n):
            output.append(i)
            output.append(-i)

        return output
  

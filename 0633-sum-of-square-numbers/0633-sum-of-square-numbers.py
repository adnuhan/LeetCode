import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        length=math.ceil(math.sqrt(c))
        array=[i for i in range(length+1)]
        left=0
        right=length
        while left<=right:
            current=array[left]**2 +array[right]**2
            if current==c:
                return True
            elif current>c:
                right=right-1
            else:
                left=left+1
        return False

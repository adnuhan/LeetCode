class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        odd = 1
        rem = num
        while rem >= odd:
            rem = rem - odd
            odd += 2
        if rem == 0:
            return True
        return False
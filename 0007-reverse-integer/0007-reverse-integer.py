class Solution(object):
    def reverse(self, x):
        rev_x = 0
        if x < 0:
            x = x * -1
            sign = -1
        else:
            sign = 1

        while x != 0:
            last = x % 10
            rev_x = (rev_x * 10) + last
            x = x // 10
        if rev_x >= 2147483647:
            return 0
        else:
            return rev_x * sign
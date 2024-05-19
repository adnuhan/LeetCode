class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_index = 0
        right_index = (len(s) - 1)

        while left_index < right_index:
            if s[left_index] != s[right_index]:
                skip_left = s[left_index + 1: right_index + 1]
                skip_right = s[left_index : right_index]
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
            left_index += 1
            right_index -= 1
        return True
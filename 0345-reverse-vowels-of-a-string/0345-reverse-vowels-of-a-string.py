class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        vowels = "aeiouAEIOU"
        x = 0
        y = len(s_list) - 1
        first = ''
        while x <= y:
            if s_list[x] in vowels:
                first = s_list[x]
                if s_list[y] in vowels:
                    s_list[x] = s_list[y]
                    s_list[y] = first
                    x += 1
                y -= 1
            else:
                x += 1
        return "".join(s_list)

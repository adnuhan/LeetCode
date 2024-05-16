class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == word.upper():
            return True
        elif word == word.lower():
            return True
        elif word == word.capitalize():
            return True
        else:
            return False
        
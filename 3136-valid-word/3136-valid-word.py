class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        vowel = "aeiouAEIOU"
        character = "@#$"
        consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        
        vowels = 0
        consonants = 0
        
        for i in range(len(word)):
            if word[i] in character:
                return False
            elif word[i] in vowel:
                vowels += 1
            elif word[i] in consonant:
                consonants += 1
        
        if len(word) >= 3 and vowels > 0 and consonants > 0:
            return True
        else:
            return False

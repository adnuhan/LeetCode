class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        
        acronym = ""
        
        for word in words:
            acronym += word[0]
        
        if acronym == s:
            return True
        
        return False
            
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
    
        occurrences = list(Counter(s).values())

        if([occurrences[0]] * len(occurrences) == occurrences):
            return True
        else:
            return False

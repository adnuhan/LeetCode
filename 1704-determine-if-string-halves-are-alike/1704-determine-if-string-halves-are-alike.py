class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        a = 0
        b = 0
        j = len(s) - 1
        
        for i in range(len(s) // 2):
            if s[i].lower() in "aeiou":
                a += 1
            if s[j].lower() in "aeiou":
                b += 1
            j -= 1
                
        return a == b
    
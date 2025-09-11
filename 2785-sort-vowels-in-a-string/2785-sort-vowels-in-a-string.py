class Solution:
    def sortVowels(self, s: str) -> str:
            
        vowels = set("aeiouAEIOU")
        
        extracted = [ch for ch in s if ch in vowels]
        extracted.sort()
        
        result = []
        idx = 0
        for ch in s:
            if ch in vowels:
                result.append(extracted[idx])
                idx += 1
            else:
                result.append(ch)
        
        return "".join(result)

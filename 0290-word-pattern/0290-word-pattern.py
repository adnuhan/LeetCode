class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        hashmap = {}
        s = s.split()

        if len(pattern) != len(s):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in hashmap and s[i] not in hashmap.values():
                hashmap[pattern[i]] = s[i]
            elif pattern[i] not in hashmap or hashmap[pattern[i]] != s[i]:
                return False

        return True

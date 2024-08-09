class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        hashmap_s = {}
        hashmap_t = {}

        for i in range(len(s)):
            if s[i] in hashmap_s and hashmap_s[s[i]] != t[i] or t[i] in hashmap_t and hashmap_t[t[i]] != s[i]:
                return False
            hashmap_s[s[i]] = t[i]
            hashmap_t[t[i]] = s[i]

        return True

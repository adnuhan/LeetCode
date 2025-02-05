class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True  # No swap needed

        # Dictionary to store mismatched characters
        mismatches = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mismatches.append((s1[i], s2[i]))
                # Early exit if more than 2 mismatches
                if len(mismatches) > 2:
                    return False

        # Check if exactly two mismatches are inverse pairs
        return len(mismatches) == 2 and mismatches[0] == mismatches[1][::-1]

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

        m = len(languages)
        user_languages = [set(l) for l in languages]

        candidates = set()
        for u, v in friendships:
            u -= 1  # convert to 0-based
            v -= 1
            if not (user_languages[u] & user_languages[v]):  # no common language
                candidates.add(u)
                candidates.add(v)

        if not candidates:
            return 0

        min_teach = float("inf")
        for lang in range(1, n+1):
            already_knows = sum(1 for u in candidates if lang in user_languages[u])
            min_teach = min(min_teach, len(candidates) - already_knows)

        return min_teach

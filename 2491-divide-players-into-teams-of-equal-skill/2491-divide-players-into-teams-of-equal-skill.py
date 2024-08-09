class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        if len(skill) == 2:
            return skill[0] * skill[1]

        skill.sort()
        i = 0
        j = len(skill) - 1
        output = 0

        while i < j:
            output += skill[i] * skill[j]
            i += 1
            j -= 1
            if skill[0] + skill[-1] != skill[i] + skill[j]:
                return -1

        return output

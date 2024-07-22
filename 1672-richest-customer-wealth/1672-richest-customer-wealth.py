class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        output = 0

        for wealth in accounts:
            if sum(wealth) > output:
                output = sum(wealth)
    
        return output

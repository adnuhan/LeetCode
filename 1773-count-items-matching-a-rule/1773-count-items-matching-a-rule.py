class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        index = 0
        output = 0        
        
        if ruleKey == "type":
            index = 0
        elif ruleKey == "color":
            index = 1
        else:
            index = 2
            
        for item in items:
            if item[index] == ruleValue:
                output += 1
            
        return output
            
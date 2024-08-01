class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        output = 0
        
        for detail in details:
            if int(detail[11:13]) > 60:
                output += 1
            
        return output

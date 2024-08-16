class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        change = []

        for bill in bills:
            if bill == 5:
                change.append(5)
            elif bill == 10 and 5 in change:
                change.append(10)
                change.remove(5)
            elif bill == 20 and 5 in change and 10 in change:
                change.append(20)
                change.remove(5)
                change.remove(10)
            elif bill == 20 and change.count(5) > 2:
                change.append(20)
                change.remove(5)
                change.remove(5)
                change.remove(5)
            else:
                return False
        
        return True

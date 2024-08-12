class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        i = 0
        j = 0
        
        if len(name) > len(typed):
            return False
        
        if len(name) == len(typed):
            return name == typed

        if name[0] != typed[0] or name[-1] != typed[-1]:
            return False
        
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
            
        return True
    

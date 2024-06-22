class Solution:
    def clearDigits(self, s: str) -> str:
        
        numbers = "1234567890"
        character = 0
        s_list = list(s)
        
        while character <= len(s_list) - 1:
            digit = s_list[character]
            
            if s_list[character] in numbers:
                del s_list[character - 1]
                s_list.remove(digit)
                character -= 2

            character += 1

        return "".join(s_list)
        
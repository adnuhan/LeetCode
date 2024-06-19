class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit_str = ""
        
        for i in digits:
            digit_str += str(i)
        new_digit = str(int(digit_str) + 1)
        digit_list = [int(i) for i in new_digit]
        
        return list(digit_list)

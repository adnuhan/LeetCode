class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num_list = list(s)
        index = 0
        integer = 0

        for i in num_list:
            if index == len(num_list) - 1:
                integer += roman[i]
                break
            elif num_list[index] == 'I' and num_list[index + 1] == 'V' or num_list[index] == 'I' and num_list[index + 1] == 'X':
                integer += (roman[num_list[index + 1]] - roman[num_list[index]])
                num_list.remove(num_list[index + 1])
                index += 1
            elif num_list[index] == 'X' and num_list[index + 1] == 'L' or num_list[index] == 'X' and num_list[index + 1] == 'C':
                integer += roman[num_list[index + 1]] - roman[num_list[index]]
                num_list.remove(num_list[index + 1])
                index += 1
            elif num_list[index] == 'C' and num_list[index + 1] == 'D' or num_list[index] == 'C' and num_list[index + 1] == 'M':
                integer += roman[num_list[index + 1]] - roman[num_list[index]] 
                num_list.remove(num_list[index + 1])
                index += 1
            else:
                integer += roman[i]
                index += 1
        return integer
        

class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        number_list = []
        output_number = []
        output = ""

        for i in number:
            if i != "-" and i != " ":
                number_list.append(i)

        while len(number_list) >= 2:
            if len(number_list) > 4:
                output_number.append(number_list[:3])
                output_number.append("-")
                del number_list[:3]
            elif len(number_list) == 4:
                output_number.append(number_list[:2])
                output_number.append("-")
                del number_list[:2]
            elif len(number_list) == 3:
                output_number.append(number_list[:3])
                del number_list[:3]
            elif len(number_list) == 2:
                output_number.append(number_list[:2])
                del number_list[:2]
        
        for j in output_number:
            output += "".join(j)
        
        return output
        
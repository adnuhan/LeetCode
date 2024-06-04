class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """

        title_list = title.split(' ', (len(title)))
        output = ""
        
        for i in range(len(title_list)):
            if len(output) > 0:
                output += " "
            if len(title_list[i]) > 2:
                output += title_list[i].capitalize()
            else:
                output += title_list[i].lower()
            
        
        return output

        
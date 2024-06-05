class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        """
        available_chairs = 0
        chairs_needed = 0

        for i in s:
            if i == "E":
                available_chairs += 1
            else:
                available_chairs -= 1
            chairs_needed = max(available_chairs, chairs_needed)
            
        return chairs_needed  

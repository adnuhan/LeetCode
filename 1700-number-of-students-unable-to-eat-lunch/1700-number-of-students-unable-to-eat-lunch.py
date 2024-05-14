class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        result = len(students)
        choice = Counter(students)
        
        for sandwich in sandwiches:
            if choice[sandwich] > 0:
                result -= 1
                choice[sandwich] -= 1
            else:
                return result
        return result
        
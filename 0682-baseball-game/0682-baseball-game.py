class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record = []
        total = 0
        for i in operations:
            if i == "C":
                record.pop()
            elif i == "D":
                record.append(int(record[(len(record) - 1)]) * 2)
            elif i == "+":
                record.append(int(record[(len(record) - 1)]) + int(record[len(record) - 2]))
            else:
                record.append(i)
        for i in record:
            total += int(i)
        return total        
class MinStack(object):

    def __init__(self):
        self.list = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.list.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.list.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.list[len(self.list) - 1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.list)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
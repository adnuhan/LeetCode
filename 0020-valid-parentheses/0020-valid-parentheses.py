class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {')': '(', ']': '[', '}': '{'}
        for item in s:
            if item in parentheses:
                if stack and stack[-1] == parentheses[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
        return True if not stack else False
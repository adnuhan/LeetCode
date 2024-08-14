class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []

        for n in s:
            if len(stack) > 0 and stack[-1] == n:
                stack.pop()
            else:
                stack.append(n)

        return "".join(stack)
        

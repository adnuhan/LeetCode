class Solution:
    def simplifyPath(self, path: str) -> str:
  
        path = path.split('/')
        stack = []

        for n in path:
            if n == '.' or n == '':
                continue
            if n == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(n)

        return '/' + '/'.join(stack)

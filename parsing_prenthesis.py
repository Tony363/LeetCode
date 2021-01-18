
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if not stack:
                    return False
                elif i!= ')}]'['({['.index(stack.pop())] :
                    return False
        return len(stack) ==0
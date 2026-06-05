class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_to_closed = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:  # We have closed bracket
                if not stack:  # stack is empty, so bracket is closing nothing
                    return False
                bracket = stack.pop()  # This will be an open bracket
                if open_to_closed[bracket] != c:
                    return False

        return not stack
                
        
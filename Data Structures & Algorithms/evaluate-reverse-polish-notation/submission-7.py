import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                second = stack.pop()
                first = stack.pop()
                res = first + second
                stack.append(res)
            elif token == '-':
                second = stack.pop()
                first = stack.pop()
                res = first - second
                stack.append(res)
            elif token == '*':
                second = stack.pop()
                first = stack.pop()
                res = first * second
                stack.append(res)
            elif token == '/':
                second = stack.pop()
                first = stack.pop()
                res = first / second
                if res >= 0:
                    res = math.floor(res)
                else:
                    res = math.ceil(res)
                stack.append(res)
            else:
                stack.append(int(token))

        return stack[-1]
        
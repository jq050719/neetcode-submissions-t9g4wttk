class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # Store indices of temperatures
        # Don't change the stack if indices of temperatures are in descending order
        # Like in Example 2: temperatures[0] >= temperatures[1] >= temperatures[2]
        # When comparing, we want temperatures[stack[-1]] (top element of stack)...
        # ...to be greater than or equal to temperatures[i], the element we are looking at
        # So, if temperatures[stack[-1]] < temperatures[i], pop off the stack
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)

        return res
        
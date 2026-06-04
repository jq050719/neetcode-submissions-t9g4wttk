class Solution:
    def trap(self, height: List[int]) -> int:
        # We can't trap any water at start or end of array
        # amount of water trapped at i = 
        # min(max height to left of i, max height to right of i) - height[i]
        n = len(height)
        max_to_left = [0] * n
        max_to_right = [0] * n

        # Fill max_to_left
        left_biggest = height[0]
        for i in range(1, n):
            max_to_left[i] = max(left_biggest, height[i - 1])
            left_biggest = max(left_biggest, height[i])

        # Fill max_to_right
        right_biggest = height[n - 1]
        for i in range(n - 2, -1, -1):
            max_to_right[i] = max(right_biggest, height[i + 1])
            right_biggest = max(right_biggest, height[i])

        res = 0
        for i in range(n):
            water = min(max_to_left[i], max_to_right[i]) - height[i]
            if water > 0:
                res += water

        return res
        
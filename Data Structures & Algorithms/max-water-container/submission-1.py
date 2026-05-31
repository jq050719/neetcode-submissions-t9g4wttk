class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Given heights[i] and heights[j], where i < j
        # Amount of water = min(heights[i], heights[j]) * (j - i)
        res = 0
        left, right = 0, len(heights) - 1
        while left < right:
            water = min(heights[left], heights[right]) * (right - left)
            res = max(res, water)
            # When incrementing left and decrementing right, we must go to taller columns
            # We must increment the smaller of left and right
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return res
        
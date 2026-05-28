class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Use the fact that numbers is non-decreasing
        left, right = 0, len(numbers) - 1
        while left < right:
            res = numbers[left] + numbers[right]
            if res == target:
                return [left + 1, right + 1]  # Since 1-indexed
            elif res < target:
                # In this case, we need to check larger numbers
                # Decrementing right never gives a larger result
                # So, increment left
                left += 1
            else:  # res > target
                # In this case, we need to check smaller numbers
                # Incrementing left never gives a smaller result
                # So, decrement right
                right -= 1
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            # Ignore non-alphanumeric characters
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1

            # Now check
            if s[l].lower() != s[r].lower():  # Use .lower() because case-insensitive
                return False

            l += 1
            r -= 1

        return True
        
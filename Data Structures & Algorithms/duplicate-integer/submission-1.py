class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        s = set(nums)
        return n != len(s)
        
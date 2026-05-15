class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_so_far = 0
        set_of_nums = set(nums)
        for num in set_of_nums:
            if num - 1 not in set_of_nums:  # this means a longer sequence cannot be created
                seq = [num]
                while seq[-1] + 1 in set_of_nums:  # last element plus one is just the next element required in sequence
                # if this element not in nums, we cannot add to the sequence
                    seq.append(seq[-1] + 1)
                max_so_far = max(max_so_far, len(seq))

        return max_so_far

            
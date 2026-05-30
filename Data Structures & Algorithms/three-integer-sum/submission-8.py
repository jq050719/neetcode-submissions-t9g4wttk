class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # When does a triplet sum up to 0?
        # Take nums[i]. We need nums[j] + nums[k] = -nums[i]
        # -nums[i] is the target
        # Sorting nums will make it easier to use two pointers, O(n log n)
        nums.sort()

        res = []
        n = len(nums)
        i = 0
        while i < n - 2:  # Can check at most nums[n-3], nums[n-2], nums[n-1]
            target = -nums[i]
            j, k = i + 1, n - 1
            # Note that nums is sorted
            while j < k:
                two_sum = nums[j] + nums[k]
                if two_sum == target:
                    res.append([nums[i], nums[j], nums[k]])
                    # Cannot have duplicates
                    # Ensure new j and k result in different values for nums[j] and nums[k]
                    curr_j = nums[j]
                    while curr_j == nums[j] and j < k:
                        j += 1
                    curr_k = nums[k]
                    while curr_k == nums[k] and j < k:
                        k -= 1
                # If two_sum > target, then we need to decrease one of the operands
                # Since nums is sorted, decrement k
                elif two_sum > target:
                    k -= 1
                # Otherwise, two_sum < target, we need to increase one of the operands
                # Since nums is sorted, increment j
                else:
                    j += 1

            # Ensure new i results in different value for nums[i]
            curr_i = nums[i]
            while curr_i == nums[i] and i < n - 2:
                i += 1

        return res
        
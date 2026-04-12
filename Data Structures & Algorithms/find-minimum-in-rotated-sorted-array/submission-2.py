class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2       # get midpoint
            # we are looking for the index i s.t.
            # nums[i-1] > nums[i] (or nums[i] > nums[i+1])
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            # list was ascending.
            # minimum in right half of list if middle element greater than right-most
            elif nums[mid] > nums[high]:
                low = mid + 1
            # list was ascending.
            # minimum in left half of list if middle element less than left-most
            elif nums[mid] < nums[low]:
                high = mid - 1
            # Otherwise, nums[low] <= nums[mid] <= nums[high]
            # Then, no rotations
            else:
                return nums[low]

        
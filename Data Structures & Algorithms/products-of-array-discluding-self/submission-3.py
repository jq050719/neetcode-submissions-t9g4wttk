class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # create an array of product of elements BEFORE element at index i
        left_products = [1] * n
        # create an array of product of elements AFTER element at index i
        right_products = [1] * n
        # fill left products array
        for i in range(1, n):
            left_products[i] = nums[i - 1] * left_products[i - 1]
        # fill right products array
        for i in range(n - 2, -1, -1):
            right_products[i] = nums[i + 1] * right_products[i + 1]
        
        res = [left_products[i] * right_products[i] for i in range(n)]
        return res
        
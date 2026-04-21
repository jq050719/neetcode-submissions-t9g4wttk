class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = {}
        freq_to_num = [[] for _ in range(len(nums) + 1)]
        # create mapping of number to how many times it appears
        for num in nums:
            num_to_freq[num] = num_to_freq.get(num, 0) + 1
        # create list where index represents frequency of a number
        # at each index i is the list of all numbers appearing i times
        for num, count in num_to_freq.items():
            freq_to_num[count].append(num)

        # iterate from n = len(nums) to 1, and return when we have k elements
        res = []
        for i in range(len(nums), -1, -1):
            for num in freq_to_num[i]:
                res.append(num)
                if len(res) == k:
                    return res

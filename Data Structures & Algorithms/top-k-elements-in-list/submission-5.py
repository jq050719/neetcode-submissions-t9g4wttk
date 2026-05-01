class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map all numbers to their frequency
        num_to_freq = {}
        for num in nums:
            num_to_freq[num] = num_to_freq.get(num, 0) + 1
        # map frequency to numbers
        # a number can appear at most len(nums) times
        freq_to_num = [[] for _ in range(len(nums) + 1)]
        for num in num_to_freq:
            freq = num_to_freq[num]
            freq_to_num[freq].append(num)

        res = []
        for i in range(len(nums), -1, -1):
            for j in range(len(freq_to_num[i])):
                res.append(freq_to_num[i][j])
                if len(res) == k:
                    return res

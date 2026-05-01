class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key: counts of each lowercase letter, value: sublist
        res = defaultdict(list)
        for s in strs:
            counts = [0] * 26  # counts of each letter: a = 0, b = 1,..., z = 25
            for c in s:
                # use the fact that strs[i] is made of lowercase letters
                counts[ord(c) - ord('a')] += 1
            # cannot use list as a dictionary key, cast to tuple
            res[tuple(counts)].append(s)

        return list(res.values())
        
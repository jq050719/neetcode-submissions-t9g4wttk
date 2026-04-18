class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # otherwise, s and t have same length
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        return sorted_s == sorted_t

        
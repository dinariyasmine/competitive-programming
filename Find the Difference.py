class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        for char_s,char_t in zip(sorted_s,sorted_t):
            if char_s != char_t:
                return char_t
        return sorted_t[-1]
        
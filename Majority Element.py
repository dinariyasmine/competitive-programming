
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = None
        cpt = 0
        for num in nums:
            if cpt == 0:
                cand = num
            if num == cand:
                cpt += 1
            else:
                cpt -= 1
        cpt = sum(1 for num in nums if num == cand)
        if cpt > len(nums) // 2:
            return cand
        else:
            return -1

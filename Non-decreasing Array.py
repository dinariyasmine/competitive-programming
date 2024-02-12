
from ast import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cpt = 0
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                cpt += 1
                if i > 0 and nums[i + 1] < nums[i - 1]:
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i + 1]
        return cpt <= 1

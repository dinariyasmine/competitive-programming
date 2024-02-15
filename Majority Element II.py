class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = (len(nums)) //3
        output = []
        for i in set(nums):
            if nums.count(i) > n:
                output.append(i)
        return output

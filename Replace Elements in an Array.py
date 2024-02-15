class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        for operation in operations:
                index = nums.index(operation[0])
                nums[index] = operation[1]
        return nums
        

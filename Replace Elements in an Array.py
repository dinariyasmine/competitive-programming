class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        index_map = {num: i for i, num in enumerate(nums)}
        
        for operation in operations:
            if operation[0] in index_map:
                old_num_index = index_map[operation[0]]
                nums[old_num_index] = operation[1]
                index_map.pop(operation[0])
                index_map[operation[1]] = old_num_index
        return nums
        

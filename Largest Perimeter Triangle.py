from typing import List

class Solution:
    # does it make a triangle first ?
    def can_form_triangle(self, a, b, c) -> bool:
        return a + b > c and a + c > b and b + c > a
    
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True) 
        for i in range(len(nums) - 2):
            if self.can_form_triangle(nums[i], nums[i + 1], nums[i + 2]):
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0 

from typing import List

class Solution:
    # does it make a triangle first ?
    def can_form_triangle(self, a, b, c) -> bool:
        return a + b > c and a + c > b and b + c > a
    
    def largestPerimeter(self, nums: List[int]) -> int:
        maxi = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if self.can_form_triangle(nums[i], nums[j], nums[k]):
                        perimeter = nums[i] + nums[j] + nums[k]
                        maxi = max(maxi , perimeter)
        return maxi

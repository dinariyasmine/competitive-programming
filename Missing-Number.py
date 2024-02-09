from ast import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_dict = {} #create empty dictionnary
        for num in nums :
            num_dict[num] = True 
        n = len(nums)
        for num in range(n + 1):
            if num not in num_dict: #numbers to find the missing one
                return num 